import web3 
from eth_utils import decode_hex,to_checksum_address
from  graphviz import Digraph
from parsers import SwapEventParser
import abis
import sys,os 


if len(sys.argv) < 2:
    print('python main.py <tx hash> [web3 http endpoint]\n')
    sys.exit()


# Setup 0: Create Web3 Instance

default_web3_http_endpoint = 'http://127.0.0.1:8545'  
web3_http_endpoints = default_web3_http_endpoint

if len(sys.argv) >= 3:
    web3_http_endpoints = sys.argv[2]

w3=web3.Web3(web3.HTTPProvider(web3_http_endpoints))

print('\nNotice: using web3 http endpoint : {}\n'.format(web3_http_endpoints)) 

# Setup 1: Create 1inch.exchange v2  web3 contract instance 

one_inch_exchange_v2_addr = '0x111111125434b319222CdBf8C261674aDB56F3ae'

one_inch = w3.eth.contract(
    address=one_inch_exchange_v2_addr,
    abi = abis.abi_1inch_exchange_v2
)


# get Transaction Hash 

input_tx_hash = sys.argv[1] 

print('Fetching transaction from web3 provider...\n')
tx = w3.eth.getTransaction(input_tx_hash)



# Step 0:  Preflights, is this tx a swap on 1inch exchange? 

# TODO: swap on 1inch.exchange through another contract ? 
if tx['to'] != one_inch_exchange_v2_addr:
    raise Exception("May not be a 1inch v2 swap transaction, tx.to is {}, rather than {}".format(tx.to,one_inch_exchange_v2_addr))

# decode transaction input data
decoded_input = one_inch.decode_function_input(tx['input'])

# calling function name 
fn_name = decoded_input[0].fn_name 
# calling arguments 
one_inch_caller = decoded_input[1]['caller']
src_receiver, dst_receiver= decoded_input[1]['desc'][2:4]


# we take only two kinds of function calls into account: 
#   - discountedSwap : swap with chi burnt  
#   - swap:  swap without chi burnt   

if fn_name not in ['swap','discountedSwap']:
    # TODO: possible internal transaction ? 
    raise Exception("May not be a 1inch swap transaction, {} is called.".format(fn_name))



# Okay, Let's start to parse event logs... 


# Step 1: Get Receipts 
receipts = w3.eth.getTransactionReceipt(input_tx_hash).logs

# Step 2: parse event logs as swaps 

# create a  parser
parse = SwapEventParser(w3)

# swap nodes 
# each node is simply a string which describes the swap
# 
# eg: 
#    Weth: swap 60.0 ETH(ether) for 60.0 WETH(Wrapped Ether)
# 
swap_nodes = []

# the summary of the swap
# parsed from 1inch event log.
swap_summary = ''

for ind in range(0,len(receipts)):
    # print progress 
    print('parsing  in progress ... {}/{}'.format(ind+1, len(receipts)))

    log = receipts[ind]
    t = parse.parse_addr(log['address'])
    if t == 'other-contract':
        continue 
    elif t == '1inch-exchange-v2':
        # parse swap summary 
        swap = parse.parse_1inch_v2_swap(log)
        if swap is not None:
            swap_summary = 'Swap Summary: ' + parse.describe_swap(swap)
        continue 
    elif t == 'Kyber':
        swap = parse.parse_kyber_trade_event(log)
    elif t.startswith('curve.fi'):
        swap = parse.parse_curve(log)
    elif t == 'Bancor':
        swap = parse.parse_bancor(log)
    elif t == 'Uniswap-V2':
        swap = parse.parse_uniswap_v2_swap_event(log) 
    elif t == 'SushiSwap':
        swap = parse.parse_sushi_swap_event(log)
    elif t == 'Balancer':
        swap = parse.parse_balancer(log) 
    elif t == 'Uniswap-V1':
        swap = parse.parse_uniswap_v1(log)  
    elif t == 'Mooniswap':
        swap = parse.parse_mooniswap_pair(log)
    elif t == 'Weth':
        swap = parse.parse_weth(log)
    elif t == 'Shell':
        swap = parse.parse_shell(log) 
    elif t == 'Oasis':
        swap = parse.parse_oasis(log)  
    elif t == '0x-V2':
        swap = parse.parse_0x_v2(log) 
    elif t == '0x-V3':
        swap = parse.parse_0x_v3(log)
    elif t == 'LuaSwap':
        swap = parse.parse_uniswap_v2_swap_event(log)
    elif t.startswith('Compound'):
        swap = parse.parse_ctoken(log)
    else:
        # EOA .. etc 
        continue

    if swap is not None:
        actor = swap[-1]
        if actor not in[ one_inch_exchange_v2_addr, one_inch_caller, src_receiver, dst_receiver]:
            # this could be an internal transaction in another exchange 
            # and should not be part of our swap path 
            continue
        
        swap_nodes.append(t + ': ' + parse.describe_swap(swap))   
            

# Step 3: Generate Dot Graph from swaps 
dot = Digraph(comment='Swap Path for {} in dot.'.format(input_tx_hash)) 

# node index 
node_indices = [i for i in range(0,len(swap_nodes))]

# nodes 
[ dot.node(str(i),label=swap_nodes[i],shape='box') for i in node_indices ]

# edges 
[ dot.edge(str(s),str(e)) for s,e in zip(node_indices,node_indices[1:]) ]


print('\n\nSwap Graph of {} : \n'.format(input_tx_hash))

print(swap_summary + '\n')

# Last Step: output ascii graph with graph-easy 

import subprocess 

x = subprocess.Popen(('echo', dot.source), stdout=subprocess.PIPE)     
output = subprocess.check_output(['graph-easy','--ascii'],stdin=x.stdout) 
print(output.decode('utf-8'))


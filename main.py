import web3 
from eth_utils import decode_hex,to_checksum_address
from  graphviz import Digraph
from parsers import SwapEventParser
import abis
import sys,os 


def print_usage():
    print('python main.py <tx hash> [web3 http endpoint]\n')
    sys.exit()

if len(sys.argv) < 2:
    print_usage()

default_web3_http_endpoint = 'http://127.0.0.1:8545'  
web3_http_endpoints = default_web3_http_endpoint

if len(sys.argv) >= 3:
    web3_http_endpoints = sys.argv[2]

print('Notice: using web3 http endpoint : {}\n'.format(web3_http_endpoints)) 

input_tx_hash = sys.argv[1] 

w3=web3.Web3(web3.HTTPProvider(web3_http_endpoints))

one_inch_exchange_v2_addr = '0x111111125434b319222CdBf8C261674aDB56F3ae'

one_inch = w3.eth.contract(
    address=one_inch_exchange_v2_addr,
    abi = abis.abi_1inch_exchange_v2
)

print('Fetching transaction from web3 provider...\n')

# Step 0:  Preflights, is this tx a swap on 1inch exchange? 

tx = w3.eth.getTransaction(input_tx_hash)

# TODO: swap on 1inch.exchange through another contract ? 
if tx['to'] != one_inch_exchange_v2_addr:
    raise Exception("May not be a 1inch v2 swap transaction, tx.to is {}, rather than {}".format(tx.to,one_inch_exchange_v2_addr))

# initiator of the tx 
initiator = tx['from']

# decode input data
decoded_input = one_inch.decode_function_input(tx['input'])

fn_name = decoded_input[0].fn_name 

# we take only two kinds of function calls into account: 
#   - discountedSwap : swap with chi burnt  
#   - swap:  swap without chi burnt   

if fn_name not in ['swap','discountedSwap']:
    # TODO: possible internal transaction ? 
    raise Exception("May not be a 1inch swap transaction, {} is called.".format(fn_name))


# args
one_inch_caller = decoded_input[1]['caller']
desc = decoded_input[1]['desc']

(src_token,dst_token, src_receiver, dst_receiver, amount_in)=desc[:5]


# Step 1: Get Receipts 
receipts = w3.eth.getTransactionReceipt(input_tx_hash).logs

# Step 2: parse event logs as swaps 

# create a  parser
parse = SwapEventParser(w3)

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
    elif t == 'kyber-proxy':
        swap = parse.parse_kyber_trade_event(log)
        if swap is not None:
            swap_nodes.append('Kyber: ' + parse.describe_swap(swap))
    elif t.startswith('curve.fi'):
        swap = parse.parse_curve(log)
        if swap is not None:
            swap_nodes.append(t + ': ' + parse.describe_swap(swap))
    elif t == 'bancor-network':
        swap = parse.parse_bancor(log)
        if swap is not None:
            swap_nodes.append('Bancor: '+ parse.describe_swap(swap))
    elif t == 'uniswap-v2-pair':
        swap = parse.parse_uniswap_v2_swap_event(log)
        if swap is not None:
            swap_nodes.append('Uniswap-V2: '+ parse.describe_swap(swap))   
    elif t == 'sushiswap-pair':
        swap = parse.parse_sushi_swap_event(log)
        if swap is not None:
            swap_nodes.append('SushiSwap: '+ parse.describe_swap(swap))   
    elif t == 'balancer-pool':
        swap = parse.parse_balancer(log)
        if swap is not None:
            swap_nodes.append('Balancer: '+ parse.describe_swap(swap))    
    elif t == 'uniswap-v1':
        swap = parse.parse_uniswap_v1(log)
        if swap is not None:
            swap_nodes.append('Uniswap-V1: '+ parse.describe_swap(swap))    
    elif t == 'mooniswap':
        swap = parse.parse_mooniswap_pair(log)
        if swap is not None:
            swap_nodes.append('Mooniswap: '+ parse.describe_swap(swap))  
    elif t == 'weth':
        swap = parse.parse_weth(log)
        if swap is not None:
            # Notice: Only some of the Weth tx matter. 
            actor = swap[-1]
            if actor not in [ one_inch_exchange_v2_addr, one_inch_caller, src_receiver, dst_receiver]:
                # this may be an eth wrap or unwrap in another exchange.
                # and should not be part of our swap path 
                continue
            swap_nodes.append('Weth: '+ parse.describe_swap(swap))
    elif t == 'shell':
        swap = parse.parse_shell(log)
        if swap is not None:
            swap_nodes.append('Shell: '+ parse.describe_swap(swap))    
    elif t == 'oasis':
        swap = parse.parse_oasis(log)
        if swap is not None:
            swap_nodes.append('Oasis: '+ parse.describe_swap(swap))     
    elif t == '0x-v2':
        swap = parse.parse_0x_v2(log)
        if swap is not None:
            swap_nodes.append('0x: '+ parse.describe_swap(swap))   
    elif t == '0x-v3':
        swap = parse.parse_0x_v3(log)
        if swap is not None:
            swap_nodes.append('0x: '+ parse.describe_swap(swap))    
    elif t == '1inch-exchange-v2':
        # parse swap summary 
        swap = parse.parse_1inch_v2_swap(log)
        if swap is not None:
            swap_summary = 'Swap Summary: ' + parse.describe_swap(swap)
    elif t == 'LuaSwap':
        swap = parse.parse_uniswap_v2_swap_event(log)
        if swap is not None:
            swap_nodes.append('LuaSwap: '+ parse.describe_swap(swap))   
    elif t.startswith('Compound'):
        swap = parse.parse_ctoken(log)
        if swap is not None:
            actor = swap[-1]
            if actor not in[ one_inch_exchange_v2_addr, one_inch_caller, src_receiver, dst_receiver]:
                # this may be an ctoken mint/redeem in another exchange.
                # and should not be part of our swap path 
                continue
            swap_nodes.append(t + ': ' + parse.describe_swap(swap))   
            

# Step 3: Generate Dot Graph from swaps 

dot = Digraph(comment='Swap Path for {} in dot.'.format(input_tx_hash)) 

# node index 
node_indices = [i for i in range(0,len(swap_nodes))]

# nodes 
for i in node_indices:
    dot.node(str(i),label=swap_nodes[i],shape='box')

# edges 
edges_tuple = zip(node_indices,node_indices[1:])

[ dot.edge(str(s),str(e)) for s,e in edges_tuple ] 

print('\n\nSwap Graph of {} : \n'.format(input_tx_hash))

print(swap_summary + '\n')

# Last Step: output ascii graph with graph-easy 

import subprocess 

x = subprocess.Popen(('echo', dot.source), stdout=subprocess.PIPE)     
output = subprocess.check_output(['graph-easy','--ascii'],stdin=x.stdout) 
print(output.decode('utf-8'))


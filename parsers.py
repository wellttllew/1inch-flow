import web3
from eth_utils import decode_hex, to_checksum_address,event_abi_to_log_topic
from hash_of_code import compute_code_sha256_hash
import abis


# hash of contract codes
# check hash_of_code.py for more details
_uniswap_v2_pair_code_hash = '8b5db55fa9ab3b9527508d4abe0b39eb588bf310270c8e04b3f38214e8ba63b4'
_sushiswap_pair_code_hash = 'fb1fb4a7cf5d2213b95749762d7ab5268880008d5d0bcf1583df2aae021ceed0'
_bpool_code_hash = '3cec846b68239958db567c515d08c6b451c9317d08c074c0ba15557d4997067a'
_uniswap_v1_code_hash = 'd9aa84abc57bee6faa73a1a66b522312bfccdc28e05c6d1ba61f4c8a97989564'
_mooniswap_code_hash = 'ba1072bd1e96774734bfcb382b66d1d9a95218433805bc5fe4ad764311f86986'
_lua_swap_code_hash = 'e887974281e7a569f8c0e16f6582a97da3f224cf916bdc15dc6e8c653fabd3cf'
_dodo_code_hash = '1c79dcb138598265353cc1bf716a4a9c82e903b63f3701ddc82603ea77130bcd'


# cureve addresses
_curve_addrs = [
    # curve_abi_1
    ('0x4CA9b3063Ec5866A4B82E437059D2C43d1be596F', 'curve.fi HBTC', abis.abi_curve_1),
    ('0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7', 'curve.fi 3 Pool', abis.abi_curve_1),
    ('0x4f062658EaAF2C1ccf8C8e36D6824CDf41167956', 'curve.fi GUSD', abis.abi_curve_1),
    ('0x3eF6A01A0f81D6046290f3e2A8c5b843e738E604', 'curve.fi HUSD', abis.abi_curve_1),
    ('0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb', 'curve.fi USDK', abis.abi_curve_1),
    ('0x0f9cb53Ebe405d49A0bbdBD291A65Ff571bC83e1', 'curve.fi USDN', abis.abi_curve_1),


    # curve_abi_2
    ('0xA2B47E3D5c44877cca798226B7B8118F9BFb7A56', 'curve.fi Compound', abis.abi_curve_2),
    ('0x52EA46506B9CC5Ef470C5bf89f17Dc28bB35D85C', 'curve.fi USDT', abis.abi_curve_2),
    ('0x06364f10B501e868329afBc005b3492902d6C763', 'curve.fi PAX', abis.abi_curve_2),
    ('0x45F783CCE6B7FF23B2ab2D70e416cdb7D6055f51', 'curve.fi Y', abis.abi_curve_2),
    ('0x79a8C46DeA5aDa233ABaFFD40F3A0A2B1e5A4F27', 'curve.fi Binance', abis.abi_curve_2),
    ('0xA5407eAE9Ba41422680e2e00537571bcC53efBfD', 'curve.fi sUSDv2', abis.abi_curve_2),
    ('0x7fC77b5c7614E1533320Ea6DDc2Eb61fa00A9714', 'curve.fi SBTC', abis.abi_curve_2),
    ('0x93054188d876f558f4a66B2EF1d97d16eDf0895B', 'curve.fi REN', abis.abi_curve_2),
]

# kyber addresses 
_addr_kyber_proxy = '0x9AAb3f75489902f3a48495025729a0AF77d4b11e' 

# bancor network address 
_addr_bancor_network = '0x2F9EC37d6CcFFf1caB21733BdaDEdE11c823cCB0'

# 1 inch v2 addresses 
_addr_1inch_exchange_v2 = '0x111111125434b319222CdBf8C261674aDB56F3ae'

# shell address 
_addr_shell_1 = '0x02Af7C867d6Ddd2c87dEcec2E4AFF809ee118FBb'
_addr_shell_2 = '0x2E703D658f8dd21709a7B458967aB4081F8D3d05' 
_addr_shells = [_addr_shell_1, _addr_shell_2]

# oasis address 
_address_oasis = '0x794e6e91555438aFc3ccF1c5076A74F42133d08D'

# 0x address
_address_0x_v2 = '0x080bf510FCbF18b91105470639e9561022937712'
_address_0x_v3 = '0x61935CbDd02287B511119DDb11Aeb42F1593b7Ef'

# ETH dummy address 
_address_eth = '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'
_address_zero = '0x0000000000000000000000000000000000000000'

# Weth address
_address_weth = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
 

# ctokens 
# https://api.compound.finance/api/v2/ctoken
_addr_ctokens = [('0xf5dce57282a584d2746faf1593d3121fcac444dc',
  'Compound Sai',
  '0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359'),
 ('0x158079ee67fce2f58472a96584a73c7ab9ac95c1',
  'Compound Augur',
  '0x1985365e9f78359a9b6ad760e32412f4a445e862'),
 ('0xf650c3d88d12db855b8bf7d11be6c55a4e07dcc9',
  'Compound USDT',
  '0xdac17f958d2ee523a2206206994597c13d831ec7'),
 ('0x6c8c6b02e7b2be14d4fa6022dfd6d75921d90e4e',
  'Compound BAT',
  '0x0d8775f648430679a709e98d2b0cb6250d2887ef'),
 ('0xb3319f5d18bc0d84dd1b4825dcde5d5f7266d407',
  'Compound 0x',
  '0xe41d2489571d322189246dafa5ebde1f4699f498'),
 ('0x35a18000230da775cac24873d00ff85bccded550',
  'Compound Uniswap',
  '0x1f9840a85d5af5bf1d1762f925bdaddc4201f984'),
 ('0x70e36f6bf80a52b3b46b3af8e106cc0ed743e8e4',
  'Compound Collateral',
  '0xc00e94cb662c3520282e6f5717214004a7f26888'),
 ('0xc11b1268c1a384e55c48c2391d8d480264a3a7f4',
  'Compound Wrapped BTC',
  '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599'),
 ('0x5d3a536e4d6dbd6114cc1ead35777bab948e3643',
  'Compound Dai',
  '0x6b175474e89094c44da98b954eedeac495271d0f'),
 ('0x39aa39c021dfbae8fac545936693ac917d5e7563',
  'Compound USD Coin',
  '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'),
 ('0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5', 'Compound Ether', _address_eth )]



def get_curve_pool_name(addr):
    """is addr a curve swap contract ?

        addr : ethereum address

        returns:  pool name or None 
    """

    for a, n, _ in _curve_addrs:
        if to_checksum_address(a) == to_checksum_address(addr):
            return n
    
    return None 


def get_compound_ctoken_name(addr):

    for a,n,_ in _addr_ctokens:
        if to_checksum_address(addr) == to_checksum_address(a):
            return n 
    return None 

def get_compound_ctoken_underlying_token(addr):
    for a,_,u in _addr_ctokens:
        if to_checksum_address(addr) == to_checksum_address(a):
            return u 
    return None     


class SwapEventParser:
    """
    TODO 
    """
    def __init__(self, web3):
        self.web3 = web3

    
    def parse(self, logs, actors):
        """ parse logs 

        consume one more log entries from logs to parse a swap. 
        you should call this multiple times until len(logs_left) == 0.

        actors: the actor is 1inch.exchange caller address, 
                the user transfer its token to the actor, 
                and the actor interacts with other exchanges to perform split swaps. 

        returns: 
            logs_left: logs still not parsed 
            exchange_name: the exchange name of the swap 
            swap: (src_token, dst_token, amount_in, amount_out, sender, receiver) or None 

        """

        if len(logs) == 0:
            return [], '', None 

        # first, shell hack 
        # read parse_shell_hack for more details about this hack. 

        log_consumed, swap = self.parse_shell_hack(logs,actors)

        if swap is not None:
            return logs[log_consumed:], 'Shell Protocol', swap 
        

        # consume exactly one log event: 

        log = logs[0]
        swap = None 

        t = self.parse_addr(log['address'])

        if t == '1inch-exchange-v2':
            swap = self.parse_1inch_v2_swap(log) 
        elif t == 'Kyber':
            swap = self.parse_kyber_trade_event(log)
        elif t.startswith('curve.fi'):
            swap = self.parse_curve(log)
        elif t == 'Bancor':
            swap = self.parse_bancor(log)
        elif t == 'Uniswap-V2':
            swap = self.parse_uniswap_v2_swap_event(log) 
        elif t == 'SushiSwap':
            swap = self.parse_sushi_swap_event(log)
        elif t == 'Balancer':
            swap = self.parse_balancer(log) 
        elif t == 'Uniswap-V1':
            swap = self.parse_uniswap_v1(log)  
        elif t == 'Mooniswap':
            swap = self.parse_mooniswap_pair(log)
        elif t == 'Weth':
            swap = self.parse_weth(log)
        # elif t == 'Shell':
        #     swap = self.parse_shell(log) 
        elif t == 'Oasis':
            swap = self.parse_oasis(log)  
        elif t == '0x-V2':
            swap = self.parse_0x_v2(log) 
        elif t == '0x-V3':
            swap = self.parse_0x_v3(log)
        elif t == 'LuaSwap':
            swap = self.parse_uniswap_v2_swap_event(log)
        elif t.startswith('Compound'):
            swap = self.parse_ctoken(log)
        elif t == 'DODO':
            swap = self.parse_dodo(log)
            
        return logs[1:], t, swap 

    def parse_addr(self, addr):

        """parse addr

        A helper function to give a clue for the event log.

        returns a string as a summary of what this address is .
        """

        w3 = self.web3

        addr = to_checksum_address(addr)

        if addr == _addr_1inch_exchange_v2:
            return '1inch-exchange-v2'

        # kyber proxy
        if addr == _addr_kyber_proxy:
            return 'Kyber'

        # curve
        pool_name = get_curve_pool_name(addr)
        if pool_name is not None:
            return pool_name

        # ctoken 
        ctoken_name = get_compound_ctoken_name(addr)
        if ctoken_name is not None:
            return ctoken_name

        # bancor 
        if addr == _addr_bancor_network:
            return 'Bancor'

        if addr == _address_weth:
            return 'Weth'
        
        if addr in [_addr_shell_1,_addr_shell_2]:
            return 'Shell'

        if addr == _address_oasis:
            return 'Oasis'
        
        if addr == _address_0x_v2:
            return '0x-V2'

        if addr == _address_0x_v3:
            return '0x-V3'
        
        # TODO: use a cache to reduce web3 rpc calls 

        # get the code of the contract
        code = w3.eth.getCode(addr)

        if code.hex() == '0x':
            # external owner address
            return 'EOA'

        code_hash = compute_code_sha256_hash(code)
        if code_hash == _uniswap_v2_pair_code_hash:
            return 'Uniswap-V2'
        if code_hash == _sushiswap_pair_code_hash:
            return 'SushiSwap'
        if code_hash == _bpool_code_hash:
            return 'Balancer'
        if code_hash == _uniswap_v1_code_hash:
            return 'Uniswap-V1'
        if code_hash == _mooniswap_code_hash:
            return 'Mooniswap'
        if code_hash == _lua_swap_code_hash:
            return 'LuaSwap'
        if code_hash == _dodo_code_hash:
            return 'DODO'

        return 'other-contract'

    def parse_erc20_token(self, addr):
        """ parse erc20 token info

            addr: address of erc20 token 

            returns: (symbol,name,decimal_number)
        """

        w3 = self.web3

        # special case for eth 
        if to_checksum_address(addr) == _address_eth or to_checksum_address(addr) == _address_zero:
            return ('ETH','ether',18)

        erc20_contract = w3.eth.contract(
            address= to_checksum_address(addr),
            abi = abis.abi_erc20
        )

        symbol = erc20_contract.get_function_by_signature('symbol()')().call()
        name   = erc20_contract.get_function_by_signature('name()')().call()
        decimals = erc20_contract.get_function_by_signature('decimals()')().call()

        return (symbol,name,decimals)

    def parse_uniswap_v2_swap_event(self, log):
        """ parse uniswap v2 swap event 

            log: log return from getTransactionReceipt 

            returns: (src_token, dst_token, amount_in, amount_out, sender, receiver) or None 
        """

        w3 = self.web3

        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_uniswap_v2_pair
        )   


        # Swap (index_topic_1 address sender, uint256 amount0In, uint256 amount1In, uint256 amount0Out, uint256 amount1Out, index_topic_2 address to)
        swap_topic = '0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822'
        
        if log.topics[0].hex() != swap_topic:
            # we care only about "Swap" event 
            return None 

        token0 = c.get_function_by_signature('token0()')().call() 
        token1 = c.get_function_by_signature('token1()')().call() 


        parsed_log = c.events.Swap().processLog(log)
        args = parsed_log['args'] 

        # which token is the input token? 
        is_token0_in = args['amount0In'] > 0 and args['amount0Out'] < args['amount0In']
        
        if is_token0_in:
            return (
                    token0, 
                    token1, 
                    args['amount0In'] - args['amount0Out'],
                    args['amount1Out'] - args['amount1In'],
                    args['sender'],
                    args['to']
                    )
        else:
            return (
                    token1, 
                    token0, 
                    args['amount1In'] - args['amount1Out'],
                    args['amount0Out'] - args['amount0In'],
                    args['sender'],
                    args['to']
                    )       

    def parse_sushi_swap_event(self, log):
        """ parse sushi swap event 

            log: log return from getTransactionReceipt 

            returns: (src_token, dst_token, amount_in, amount_out, from, to) or None 
        """
        return self.parse_uniswap_v2_swap_event(log)


    def parse_kyber_trade_event(self, log):
        """ parse kyber trade event 

            log: log return from getTransactionReceipt 

            returns: (src_token, dst_token, amount_in, amount_out, from, to) or None 
        """

        w3 = self.web3


        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_kyber_proxy
        ) 

        # ExecuteTrade (index_topic_1 address trader, address src, address dest, address destAddress, uint256 actualSrcAmount, uint256 actualDestAmount, address platformWallet, uint256 platformFeeBps)
        execute_trade_topic = '0xf724b4df6617473612b53d7f88ecc6ea983074b30960a049fcd0657ffe808083'

        if log.topics[0].hex() != execute_trade_topic:
            # we care only about "ExecuteTrade" event 
            return None 

        parsed_log = c.events.ExecuteTrade().processLog(log)
        args = parsed_log['args'] 

        return (
            args['src'],
            args['dest'],
            args['actualSrcAmount'],
            args['actualDestAmount'],
            args['trader'],
            args['destAddress']
        )


    def parse_balancer(self,log):
        """ parse BPool swap event 

            log: log return from getTransactionReceipt 

            returns: (src_token, dst_token, amount_in, amount_out, from, to) or None 
        """ 

        w3 = self.web3

        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_bpool
        ) 

        # LOG_SWAP (index_topic_1 address caller, index_topic_2 address tokenIn, index_topic_3 address tokenOut, uint256 tokenAmountIn, uint256 tokenAmountOut)
        log_swap_topic = '0x908fb5ee8f16c6bc9bc3690973819f32a4d4b10188134543c88706e0e1d43378'

        if log.topics[0].hex() != log_swap_topic:
            # we care only about "LOG_SWAP" event 
            return None 
        
        parsed_log = c.events.LOG_SWAP().processLog(log)
        args = parsed_log['args']   

        return (
            args['tokenIn'],
            args['tokenOut'], 
            args['tokenAmountIn'],
            args['tokenAmountOut'],
            args['caller'],
            args['caller'] # sender and receiver is the same
        )



    def parse_bancor(self,log):
        """ parse bancor
        """


        w3 = self.web3

        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_bancor_network
        ) 

        #  Conversion (index_topic_1 address _smartToken, index_topic_2 address _fromToken, index_topic_3 address _toToken, uint256 _fromAmount, uint256 _toAmount, address _trader)
        topic = '0x7154b38b5dd31bb3122436a96d4e09aba5b323ae1fd580025fab55074334c095'

        if log.topics[0].hex() != topic:
            return None 
        
        parsed_log = c.events.Conversion().processLog(log)
        args = parsed_log['args']   

        return (
            args['_fromToken'],
            args['_toToken'], 
            args['_fromAmount'],
            args['_toAmount'],
            args['_trader'],
            args['_trader'] # sender and receiver is the same
        )



    def parse_oasis(self,log):
        """ parse oasis
        """
        """ parse bancor
        """


        w3 = self.web3


        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_oasis
        ) 

        # LogTake (bytes32 id, index_topic_1 bytes32 pair, index_topic_2 address maker, address pay_gem, address buy_gem, index_topic_3 address taker, uint128 take_amt, uint128 give_amt, uint64 timestamp)
        topic = '0x3383e3357c77fd2e3a4b30deea81179bc70a795d053d14d5b7f2f01d0fd4596f'

        if log.topics[0].hex() != topic:
            return None 
        
        parsed_log = c.events.LogTake().processLog(log)
        args = parsed_log['args']   

        return (
            args['pay_gem'],
            args['buy_gem'], 
            args['give_amt'],
            args['take_amt'],
            args['taker'],
            args['taker'] # sender and receiver is the same
        )
    

    def parse_uniswap_v1(self,log):


        w3 = self.web3

        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_uniswap_v1_exchange
        ) 

        # uniswap v1 exchange is  eth-token pair 
        token = c.get_function_by_signature('tokenAddress()')().call()

        # EthPurchase: event({buyer: indexed(address), tokens_sold: indexed(uint256), eth_bought: indexed(uint256(wei))})
        eth_purchase_topic = '0x' + event_abi_to_log_topic(c.events.EthPurchase().abi).hex()

        # TokenPurchase: event({buyer: indexed(address), eth_sold: indexed(uint256(wei)), tokens_bought: indexed(uint256)})
        token_purchase_topic = '0x' + event_abi_to_log_topic(c.events.TokenPurchase().abi).hex()

        if log.topics[0].hex() == eth_purchase_topic:
            parsed_log = c.events.EthPurchase().processLog(log)
            args = parsed_log['args']   
            return (
                token,
                _address_eth,
                args['tokens_sold'],
                args['eth_bought'],
                args['buyer'],
                args['buyer'] # sender and receiver is the same
            )
        elif log.topics[0].hex() == token_purchase_topic:
            parsed_log = c.events.TokenPurchase().processLog(log)
            args = parsed_log['args']   
            return (
                _address_eth, 
                token,
                args['eth_sold'],
                args['tokens_bought'],
                args['buyer'],
                args['buyer'] # sender and receiver is the same
            )
        else:
            return None 


    def parse_mooniswap_pair(self,log):
        """ parse mooniswap pair

            returns: (src_token, dst_token, amount_in, amount_out, from, to) or None 
        """


        w3 = self.web3

        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_mooniswap_pair
        ) 

        # event Swapped(
        #     address indexed account,
        #     address indexed src,
        #     address indexed dst,
        #     uint256 amount,
        #     uint256 result,
        #     uint256 srcBalance,
        #     uint256 dstBalance,
        #     uint256 totalSupply,
        #     address referral
        # );
        topic = '0x' + event_abi_to_log_topic(c.events.Swapped().abi).hex()

        if log.topics[0].hex() != topic:
            return None 
        parsed_log = c.events.Swapped().processLog(log)
        args = parsed_log['args']   

        return(
            args['src'],
            args['dst'],
            args['amount'],
            args['result'],
            args['account'],
            args['account']
        )




    def parse_shell(self,log):

        raise Exception('This method is deprecated, check parse_shell_hack for more details')

        w3 = self.web3
        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_shell
        ) 

        # Trade (index_topic_1 address trader, index_topic_2 address origin, index_topic_3 address target, uint256 originAmount, uint256 targetAmount)
        topic = '0xec0d3e799aa270a144d7e3be084ccfc657450e33ecea1b1a4154c95cedaae5c3'

        if log.topics[0].hex() != topic:
            return None 
        
        parsed_log = c.events.Trade().processLog(log)
        args = parsed_log['args']   

        return (
            args['origin'],
            args['target'], 
            args['originAmount'],
            args['targetAmount'],
            args['trader'],
            args['trader'] # sender and receiver is the same
        )



    def parse_curve(self,log):
        """ parse curve.fi 
            
            returns: (src_token, dst_token, amount_in, amount_out, from, to) or None 

        """


        w3 = self.web3
        addr = to_checksum_address(log['address'])


        curve_pool = [i for i in _curve_addrs if to_checksum_address(i[0]) == addr ]
        abi = curve_pool[0][2]
        
        c = w3.eth.contract(
            address= addr ,
            abi = abi  # abi
        ) 


        if abi == abis.abi_curve_2: 
            # TokenExchange: event({buyer: indexed(address), sold_id: int128, tokens_sold: uint256, bought_id: int128, tokens_bought: uint256})
            topic_token_exchange = '0x' + event_abi_to_log_topic(c.events.TokenExchange().abi).hex()

            # TokenExchangeUnderlying: event({buyer: indexed(address), sold_id: int128, tokens_sold: uint256, bought_id: int128, tokens_bought: uint256})
            topic_exchange_underlying = '0x' + event_abi_to_log_topic(c.events.TokenExchangeUnderlying().abi).hex()

            if log.topics[0].hex() == topic_token_exchange:
                parsed_log = c.events.TokenExchange().processLog(log)
                args = parsed_log['args']   
                return (
                    c.get_function_by_signature('coins(int128)')(args['sold_id']).call(),
                    c.get_function_by_signature('coins(int128)')(args['bought_id']).call(),
                    args['tokens_sold'],
                    args['tokens_bought'],
                    args['buyer'],
                    args['buyer']
                )
            elif log.topics[0].hex() == topic_exchange_underlying:
                parsed_log = c.events.TokenExchangeUnderlying().processLog(log)
                args = parsed_log['args']   
                return (
                    c.get_function_by_signature('underlying_coins(int128)')(args['sold_id']).call(),
                    c.get_function_by_signature('underlying_coins(int128)')(args['bought_id']).call(),
                    args['tokens_sold'],
                    args['tokens_bought'],
                    args['buyer'],
                    args['buyer']
                )
            else:
                return None     
        elif abi == abis.abi_curve_1:
            # TokenExchange: event({buyer: indexed(address), sold_id: int128, tokens_sold: uint256, bought_id: int128, tokens_bought: uint256})
            topic_token_exchange = '0x' + event_abi_to_log_topic(c.events.TokenExchange().abi).hex()
            if log.topics[0].hex() == topic_token_exchange:
                parsed_log = c.events.TokenExchange().processLog(log)
                args = parsed_log['args']   
                return (
                    c.get_function_by_signature('coins(uint256)')(args['sold_id']).call(),
                    c.get_function_by_signature('coins(uint256)')(args['bought_id']).call(),
                    args['tokens_sold'],
                    args['tokens_bought'],
                    args['buyer'],
                    args['buyer']
                )  
            else:
                return None    
        else:
            return None      


    def parse_weth(self,log):


        w3 = self.web3
        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_weth
        ) 

        # Deposit (index_topic_1 address dst, uint256 wad)
        deposit_topic = '0x' + event_abi_to_log_topic(c.events.Deposit().abi).hex()

        # Withdrawal (index_topic_1 address src, uint256 wad)
        withdraw_topic = '0x' + event_abi_to_log_topic(c.events.Withdrawal().abi).hex()

        if log.topics[0].hex() == deposit_topic:
            parsed_log = c.events.Deposit().processLog(log)
            args = parsed_log['args']   
            return (
                _address_eth,
                _address_weth,
                args['wad'],
                args['wad'],
                args['dst'],
                args['dst'] # sender and receiver is the same
            )
        elif log.topics[0].hex() == withdraw_topic:
            parsed_log = c.events.Withdrawal().processLog(log)
            args = parsed_log['args']   
            return (
                _address_weth, 
                _address_eth,
                args['wad'],
                args['wad'],
                args['src'],
                args['src'] # sender and receiver is the same
            )
        else:
            return None 



    def parse_1inch_v2_swap(self,log):
        """ parse 1inch v2

            returns: (src_token, dst_token, amount_in, amount_out, from, to) or None 
        """
        

        w3 = self.web3
        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_1inch_exchange_v2
        ) 

        # Swapped(
        #     address indexed sender,
        #     IERC20 indexed srcToken,
        #     IERC20 indexed dstToken,
        #     address dstReceiver,
        #     uint256 amount,
        #     uint256 spentAmount,
        #     uint256 returnAmount,
        #     uint256 minReturnAmount,
        #     uint256 guaranteedAmount,
        #     address referrer
        # );
        topic = '0x' + event_abi_to_log_topic(c.events.Swapped().abi).hex()

        if log.topics[0].hex() != topic:
            return None 
        parsed_log = c.events.Swapped().processLog(log)
        args = parsed_log['args']   

        return(
            args['srcToken'],
            args['dstToken'],
            args['amount'],
            args['returnAmount'],
            args['sender'],
            args['dstReceiver']
        )



    def describe_swap(self, swap):
        """ describe a swap in plain text.

            a swap is a tuple of (src_token, dst_token, amount_in, amount_out, from, to)

            returns desription of the swap  
        """

        w3 = self.web3
        src_token, dst_token, amount_in, amount_out, _ , _ = swap 

        src_symbol, src_name, src_decimal = self.parse_erc20_token(src_token)
        dst_symbol, dst_name, dst_decimal = self.parse_erc20_token(dst_token)

        return ( 'swap {} '.format(float(amount_in)/(10**src_decimal)) + 
                '{}({})'.format(src_symbol,src_name) + 
                ' for {} '.format(float(amount_out)/(10**dst_decimal)) + 
                '{}({})'.format(dst_symbol,dst_name) )


    def parse_0x_v2(self,log):
        """ parse 0x v2

            returns: (src_token, dst_token, amount_in, amount_out, from, to) or None 
        """
        
        w3 = self.web3
        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_0x_v2
        ) 

        # event Fill(
        #     address indexed makerAddress,         // Address that created the order.      
        #     address indexed feeRecipientAddress,  // Address that received fees.
        #     address takerAddress,                 // Address that filled the order.
        #     address senderAddress,                // Address that called the Exchange contract (msg.sender).
        #     uint256 makerAssetFilledAmount,       // Amount of makerAsset sold by maker and bought by taker. 
        #     uint256 takerAssetFilledAmount,       // Amount of takerAsset sold by taker and bought by maker.
        #     uint256 makerFeePaid,                 // Amount of ZRX paid to feeRecipient by maker.
        #     uint256 takerFeePaid,                 // Amount of ZRX paid to feeRecipient by taker.
        #     bytes32 indexed orderHash,            // EIP712 hash of order (see LibOrder.getOrderHash).
        #     bytes makerAssetData,                 // Encoded data specific to makerAsset. 
        #     bytes takerAssetData                  // Encoded data specific to takerAsset.
        # );
        topic = '0x' + event_abi_to_log_topic(c.events.Fill().abi).hex()

        if log.topics[0].hex() != topic:
            return None 
        parsed_log = c.events.Fill().processLog(log)
        args = parsed_log['args']   

        return(
            to_checksum_address('0x' + args['takerAssetData'].hex()[-40:]),
            to_checksum_address('0x' + args['makerAssetData'].hex()[-40:]),
            args['takerAssetFilledAmount'],
            args['makerAssetFilledAmount'],
            args['takerAddress'],
            args['takerAddress']
        )

    def parse_0x_v3(self,log):
        """ parse 0x v3

            returns: (src_token, dst_token, amount_in, amount_out, from, to) or None 
        """
        

        w3 = self.web3
        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_0x_v3
        ) 

        # Fill (index_topic_1 address makerAddress, 
        # index_topic_2 address feeRecipientAddress,
        #  bytes makerAssetData, 
        # bytes takerAssetData, 
        # bytes makerFeeAssetData, 
        # bytes takerFeeAssetData, 
        # index_topic_3 bytes32 orderHash, 
        # address takerAddress, 
        # address senderAddress, 
        # uint256 makerAssetFilledAmount, 
        # uint256 takerAssetFilledAmount, 
        # uint256 makerFeePaid, 
        # uint256 takerFeePaid, 
        # uint256 protocolFeePaid)
        topic = '0x' + event_abi_to_log_topic(c.events.Fill().abi).hex()

        if log.topics[0].hex() != topic:
            return None 
        parsed_log = c.events.Fill().processLog(log)
        args = parsed_log['args']   

        return(
            to_checksum_address('0x' + args['takerAssetData'].hex()[-40:]),
            to_checksum_address('0x' + args['makerAssetData'].hex()[-40:]),
            args['takerAssetFilledAmount'],
            args['makerAssetFilledAmount'],
            args['takerAddress'],
            args['takerAddress']
        )



    def parse_ctoken(self,log):


        w3 = self.web3
        c_token_addr = to_checksum_address(log['address'])

        c = w3.eth.contract(
            address= c_token_addr,
            abi = abis.abi_compound_ctoken
        ) 

        # Redeem (address redeemer, uint256 redeemAmount, uint256 redeemTokens)
        redeem_topic = '0x' + event_abi_to_log_topic(c.events.Redeem().abi).hex()

        # Mint (address minter, uint256 mintAmount, uint256 mintTokens)
        mint_topic = '0x' + event_abi_to_log_topic(c.events.Mint().abi).hex()

        if log.topics[0].hex() == redeem_topic:
            parsed_log = c.events.Redeem().processLog(log)
            args = parsed_log['args']   
            return (
                c_token_addr,
                get_compound_ctoken_underlying_token(c_token_addr),
                args['redeemTokens'],
                args['redeemAmount'],
                args['redeemer'],
                args['redeemer'] # sender and receiver is the same
            )
        elif log.topics[0].hex() == mint_topic:
            parsed_log = c.events.Mint().processLog(log)
            args = parsed_log['args']   
            return (
                get_compound_ctoken_underlying_token(c_token_addr), 
                c_token_addr,
                args['mintAmount'],
                args['mintTokens'],
                args['minter'],
                args['minter'] # sender and receiver is the same
            )
        else:
            return None 
    
    def parse_shell_hack(self, logs, actors):
        """ parse shell hack 

        Why the hack? 

        the `parse_shell` function above would fail to parse this transation: 

        0x77abc19131de0101df0dfc6fbeb02b49eaf4540f9627807ff93cb47ba2e97a13

        The contract code is here: 

        https://etherscan.io/address/0x2e703d658f8dd21709a7b458967ab4081f8d3d05#code 

        As you can see, the `Trade` Event is not emmitted for every swap. 

        The lucky part is that there will be no internal eth transfer. 
        The ERC20 transfer events are sufficient. 

        So here is the hack: 

        - Parse two types of ERC20 Transfer events:
           - actor to shell 
           - shell to actor 

        - Combine the two transfer events into a swap 


        logs: all logs of the transaction 
        actors: 1inch caller , which interacts with shell contract 

        returns:  logs_consumed, (src_token, dst_token, amount_in, amount_out, from, to)
        """

        if len(logs) < 2:
            return 0, None 

        w3 = self.web3

        # helper function for parse erc20 transfer 
        def parse_erc20_transfer(log):
            """ parse erc20 transfer

            return (from, to, value,token_addr) or None 
            """

            erc20_transfer_topic = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
            if log.topics[0].hex() != erc20_transfer_topic:
                return None 
            token_addr = to_checksum_address(log['address'])


            c = w3.eth.contract(
                address= token_addr,
                abi = abis.abi_erc20
            ) 

            parsed_log = c.events.Transfer().processLog(log)
            args = parsed_log['args']   
            return (   
                args['from'],
                args['to'],
                args['value'],
                token_addr
            )
        
        # we want to get a pair of transfer 
        #  - from actor to shell 
        #  - and from shell to actor  

        from_actor_to_shell = None 
        from_shell_to_actor = None 


        # parse actor -> shell 

        # the first log must be from actor to shell 
        from_actor_to_shell = parse_erc20_transfer(logs[0])


        if from_actor_to_shell is None:
            return 0, None 
        
        actor_addr , shell_addr, amount_in, token_in  = from_actor_to_shell

        if actor_addr not in actors or shell_addr not in _addr_shells:
            return 0, None 


        # parse shell -> actor 

        logs_consumed = 1 

        for log in logs[1:]:
            logs_consumed = logs_consumed + 1
            transfer = parse_erc20_transfer(log)
            if transfer is not None:
                if (actor_addr, shell_addr) == (transfer[1], transfer[0]):
                    from_shell_to_actor = transfer
                    break 

        if from_shell_to_actor is not None:
            _,_, amount_out, token_out  = from_shell_to_actor
            return logs_consumed, (
                token_in,
                token_out,
                amount_in,
                amount_out,
                actor_addr,
                actor_addr
            )

        return 0, None 

    def parse_dodo(self,log):
        """ parse dodo

            returns: (src_token, dst_token, amount_in, amount_out, from, to) or None 
        """
        
        w3 = self.web3
        c = w3.eth.contract(
            address= to_checksum_address(log['address']),
            abi = abis.abi_dodo
        ) 

        base_token_addr = c.get_function_by_signature('_BASE_TOKEN_()')().call()
        quote_token_addr = c.get_function_by_signature('_QUOTE_TOKEN_()')().call()

        # event BuyBaseToken(address indexed buyer, uint256 receiveBase, uint256 payQuote);
        # event SellBaseToken(address indexed seller, uint256 payBase, uint256 receiveQuote);
        
        buy_basetoken_topic = '0x' + event_abi_to_log_topic(c.events.BuyBaseToken().abi).hex()
        sell_basetoken_topic = '0x' + event_abi_to_log_topic(c.events.SellBaseToken().abi).hex()

        if log.topics[0].hex() == buy_basetoken_topic:
            parsed_log = c.events.BuyBaseToken().processLog(log)
            args = parsed_log['args']   
            return (
                quote_token_addr,
                base_token_addr,
                args['payQuote'],
                args['receiveBase'],
                args['buyer'],
                args['buyer']
            )
        elif log.topics[0].hex() == sell_basetoken_topic:
            parsed_log = c.events.SellBaseToken().processLog(log)
            args = parsed_log['args']   
            return (
                base_token_addr,
                quote_token_addr,
                args['payBase'],
                args['receiveQuote'],
                args['seller'],
                args['seller']
            )
        else:
            return None 
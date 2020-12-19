 1inch Flow 

```

 ██ ██ ███    ██  ██████ ██   ██     ███████ ██       ██████  ██     ██ 
███ ██ ████   ██ ██      ██   ██     ██      ██      ██    ██ ██     ██ 
 ██ ██ ██ ██  ██ ██      ███████     █████   ██      ██    ██ ██  █  ██ 
 ██ ██ ██  ██ ██ ██      ██   ██     ██      ██      ██    ██ ██ ███ ██ 
 ██ ██ ██   ████  ██████ ██   ██     ██      ███████  ██████   ███ ███  
                                                                     
```

A 1inch.exchange v2 swap path parser in python.   


![](demontration.gif)  


- [Quick Start](#quick-start)
  * [Option 1: Use Docker Image](#option-1-use-docker-image)
  * [Option 2: On Your Host Machine](#option-2-on-your-host-machine)
- [Examples](#examples)
  * [A typical powerful split swap on 1inch](#a-typical-powerful-split-swap-on-1inch)
  * [SushiSwap, Weth and Kyber](#sushiswap-weth-and-kyber)
  * [LuaSwap](#luaswap)
  * [Mooniswap, 0x, Uniswap-V2](#mooniswap-0x-uniswap-v2)
  * [Curve.fi , Shell and Bancor](#curvefi--shell-and--bancor)
  * [Shell cDai to Dai](#shell-cdai-to-dai)
- [TODO](#todo)(py38) 



## Quick Start 

### Option 1: Use Docker Image 


```
docker run -it --rm --network host wellttllew/1inch-flow:latest \
    0xe453018c04fdec990c909a45482234464617fb4651e0daa2c5a695cbaf4fff10 \
    http://127.0.0.1:8545
```

- replace `0xe453018c04fdec990c909a45482234464617fb4651e0daa2c5a695cbaf4fff10` with a transaction hash your are interested in ( you can find the transcations from [etherscan: 1inch.exchange v2](https://etherscan.io/address/0x111111125434b319222cdbf8c261674adb56f3ae) ).   

- replace `http://127.0.0.1:8545` with your `web3 http endpoint`, if you are using `infura`, this is in the form of `https://mainnet.infura.io/v3/xxxxxxxxxxxxxxxxxxxxx`.  



### Option 2: On Your Host Machine

> Currently, this may only work on python3.6.  

Step 0: install `graph-easy` :  
  - if you are using ubuntu, just run `apt-get install libgraph-easy-perl`  in your shell  
  - `graph-easy` is used to generate `ascii dot graph`  
 
Step 1: install dependences:    
  - run `pip3 install -r requirments.txt ` in your shell 

Then, your are ready to jet.  

```
python3 main.py 0xe453018c04fdec990c909a45482234464617fb4651e0daa2c5a695cbaf4fff10 http://127.0.0.1:8545 
``` 

> `http://127.0.0.1:8545` is web3 http endpoint, if you are using infura, this may be in the form of `https://mainnet.infura.io/v3/xxxxxxxxxxxxxxxxxxxxx`


## Examples 

Here shows some example results.. 



### A typical powerful split swap on 1inch 

```
Swap Graph of 0x98e29ec131c56acbc280daddd71899dfd0fe8f3885f1cb63b8b770e74eda1033 : 

Swap Summary: swap 200.0 ETH(ether) for 129135.09600377393 DAI(Dai Stablecoin)

+----------------------------------------------------------------------------------------------+
|                   Weth: swap 60.0 ETH(ether) for 60.0 WETH(Wrapped Ether)                    |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
|           Balancer: swap 9.0 WETH(Wrapped Ether) for 0.26501975 WBTC(Wrapped BTC)            |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
|          SushiSwap: swap 51.0 WETH(Wrapped Ether) for 1.49835395 WBTC(Wrapped BTC)           |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
|        0x-V2: swap 1.7633737 WBTC(Wrapped BTC) for 38764.59672184 DAI(Dai Stablecoin)        |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
|                   Weth: swap 60.0 ETH(ether) for 60.0 WETH(Wrapped Ether)                    |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
|             0x-V2: swap 60.0 WETH(Wrapped Ether) for 38748.6 DAI(Dai Stablecoin)             |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
|                 Kyber: swap 80.0 ETH(ether) for 51854.805287 USDC(USD Coin)                  |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
| curve.fi 3 Pool: swap 51854.805287 USDC(USD Coin) for 51711.681705784424 DAI(Dai Stablecoin) |
+----------------------------------------------------------------------------------------------+



```


### SushiSwap, Weth and Kyber 

```
Swap Graph of 0x32870cdf0be199a621fc8bad2bb7dcfcfd29f8647cdcf08629fdbbeb64b82993 : 

Swap Summary: swap 317631.909208 USDT(Tether USD) for 505.20691460183394 ETH(ether)

+-----------------------------------------------------------------------------------------+
| SushiSwap: swap 33351.350466 USDT(Tether USD) for 53.03473064846576 WETH(Wrapped Ether) |
+-----------------------------------------------------------------------------------------+
  |
  |
  v
+-----------------------------------------------------------------------------------------+
|   0x-V2: swap 77819.817756 USDT(Tether USD) for 123.7887819231687 WETH(Wrapped Ether)   |
+-----------------------------------------------------------------------------------------+
  |
  |
  v
+-----------------------------------------------------------------------------------------+
|   Weth: swap 176.82351257163444 WETH(Wrapped Ether) for 176.82351257163444 ETH(ether)   |
+-----------------------------------------------------------------------------------------+
  |
  |
  v
+-----------------------------------------------------------------------------------------+
|       Kyber: swap 28388.351885 USDT(Tether USD) for 45.216279742946696 ETH(ether)       |
+-----------------------------------------------------------------------------------------+
  |
  |
  v
+-----------------------------------------------------------------------------------------+
|       Kyber: swap 178072.389101 USDT(Tether USD) for 283.1671222872528 ETH(ether)       |
+-----------------------------------------------------------------------------------------+


```


### LuaSwap 

```

Swap Graph of 0x96972c88bde857155e4c49edc8030b458bdcb0dc813ed1db91addc792339d6df : 

Swap Summary: swap 450.0 USDC(USD Coin) for 0.02206837 WBTC(Wrapped BTC)

+---------------------------------------------------------------------+
| LuaSwap: swap 450.0 USDC(USD Coin) for 0.02206837 WBTC(Wrapped BTC) |
+---------------------------------------------------------------------+

```

### Mooniswap, 0x, Uniswap-V2 

```
Swap Graph of 0x5fffc129dda4dc11a6e212080754ff95a9794b2c5617e849501bb8d9c48613ed : 

Swap Summary: swap 8537.351057 USDC(USD Coin) for 13.62271059441722 ETH(ether)

+--------------------------------------------------------------------------------------------+
|        Mooniswap: swap 4268.675528 USDC(USD Coin) for 6.801436505590065 ETH(ether)         |
+--------------------------------------------------------------------------------------------+
  |
  |
  v
+--------------------------------------------------------------------------------------------+
|         0x-V2: swap 4268.675529 USDC(USD Coin) for 4267.617159944333 TUSD(TrueUSD)         |
+--------------------------------------------------------------------------------------------+
  |
  |
  v
+--------------------------------------------------------------------------------------------+
| Uniswap-V2: swap 4267.617159944333 TUSD(TrueUSD) for 6.821274088827156 WETH(Wrapped Ether) |
+--------------------------------------------------------------------------------------------+
  |
  |
  v
+--------------------------------------------------------------------------------------------+
|     Weth: swap 6.821274088827156 WETH(Wrapped Ether) for 6.821274088827156 ETH(ether)      |
+--------------------------------------------------------------------------------------------+



```


### Curve.fi , Shell and  Bancor 

```
Swap Graph of 0x89b405604cbe5478fc4a59d1fdb5dad0a73df0fdd8317ebc31e06b9c0ac27839 : 

Swap Summary: swap 18759.57 BNT(Bancor Network Token) for 30146.549158 USDT(Tether USD)

+----------------------------------------------------------------------------------------------+
|   Bancor: swap 3751.9139999999998 BNT(Bancor Network Token) for 6034.454361 USDC(USD Coin)   |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
|       Shell Protocol: swap 6034.454361 USDC(USD Coin) for 6029.697878 USDT(Tether USD)       |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
| Bancor: swap 6096.86025 BNT(Bancor Network Token) for 9773.890706541388 DAI(Dai Stablecoin)  |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
| curve.fi 3 Pool: swap 9773.890706541388 DAI(Dai Stablecoin) for 9794.060839 USDT(Tether USD) |
+----------------------------------------------------------------------------------------------+
  |
  |
  v
+----------------------------------------------------------------------------------------------+
|  Bancor: swap 8910.795750000001 BNT(Bancor Network Token) for 14322.790441 USDT(Tether USD)  |
+----------------------------------------------------------------------------------------------+


```

### Shell cDai to Dai 

> When you swap cDai for Dai on Shell, it would not emit a `Trade` event.  
> Some hacks are needed to make it work.  


```
Swap Graph of 0x77abc19131de0101df0dfc6fbeb02b49eaf4540f9627807ff93cb47ba2e97a13 : 

Swap Summary: swap 3056149.0709 cDAI(Compound Dai) for 151.1764466 cWBTC(Compound Wrapped BTC)

+-----------------------------------------------------------------------------------------------------+
|   Shell Protocol: swap 3056149.0709 cDAI(Compound Dai) for 63661.48901416276 DAI(Dai Stablecoin)    |
+-----------------------------------------------------------------------------------------------------+
  |
  |
  v
+-----------------------------------------------------------------------------------------------------+
|    curve.fi 3 Pool: swap 63661.48901416276 DAI(Dai Stablecoin) for 63799.238362 USDT(Tether USD)    |
+-----------------------------------------------------------------------------------------------------+
  |
  |
  v
+-----------------------------------------------------------------------------------------------------+
|             0x-V2: swap 63799.238362 USDT(Tether USD) for 3.05246369 WBTC(Wrapped BTC)              |
+-----------------------------------------------------------------------------------------------------+
  |
  |
  v
+-----------------------------------------------------------------------------------------------------+
| Compound Wrapped BTC: swap 3.05246369 WBTC(Wrapped BTC) for 151.1764466 cWBTC(Compound Wrapped BTC) |
+-----------------------------------------------------------------------------------------------------+

```

## TODO 


Pending: 

- some other exchanges in 1inch.exchange protocol   
  - `https://api.1inch.exchange/v2.0/protocols`  


Done: 

- [x] 0x77abc19131de0101df0dfc6fbeb02b49eaf4540f9627807ff93cb47ba2e97a13  
  - [Trade event is not emitted when you swap cDai for Dai on Shell](https://etherscan.io/address/0x2e703d658f8dd21709a7b458967ab4081f8d3d05#code)  
- [x] DODO:       
   - 0x9445f05a8fac6781d1ab9f138372e207dc606417ebe58b6eeed65e7db69013b5  
   - 0x3f14a928e7cc7c981df27c944a07d855f9456cdd1b8a3306726e287bde8e5723   

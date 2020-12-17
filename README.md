> TODO

1inch Flow 

A 1inch.exchange v2 swap path parser in python.   


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

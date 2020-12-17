from web3 import Web3  
import hashlib
from eth_utils import to_checksum_address


def compute_code_sha256_hash(code):
    return hashlib.sha256(bytes(code)).hexdigest()

def web3_get_code_sha256_hash(web3, addr):
    """
        web3: Web3 
        addr: address in hex string
    """
    code = web3.eth.getCode(to_checksum_address(addr))
    return compute_code_sha256_hash(code)


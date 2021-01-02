import json 
from eth_utils import to_checksum_address


def _get_canonical_address(addr):
    """ as ether may be represented with multiple addresses. 
        this function helps make it a single address.

        return addr 

    """

    if addr == '0x0000000000000000000000000000000000000000':
        return '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE' 
    
    return to_checksum_address(addr)


def validate_swap_path(whole_swap,swaps):
    """ validate the swap path

        whole_swap: the swap parsed from 1inch swap event. 
        swaps: the swaps parsed from each swap in the swap path 

        returns: true(valid swap path), false(some swap is missing in the path)
    """

    balances = dict()

    src_token, dst_token, amount_in, amount_out, sender, receiver = whole_swap

    balances[src_token] = amount_in 
    balances[dst_token] = - amount_out 

    for src_token, dst_token, amount_in, amount_out, sender, receiver in swaps:

        # if the token is ether 
        # we want to use a single address to represent it.
        src_token = _get_canonical_address(src_token)
        dst_token = _get_canonical_address(dst_token)

        if src_token not in balances:
            balances[src_token] = 0 
        if dst_token not in balances:
            balances[dst_token] = 0

        balances[src_token] = balances[src_token] -  amount_in 
        balances[dst_token] = balances[dst_token] + amount_out 

    if True:
        print('\nValidating swaps (The sum of inputs and outputs of each token should be zero.) ... :\n\n' + 
            json.dumps(balances,indent='  '))

    for key, value in balances.items():
        if value > 0:
            print("\nWarning: Some swaps may not be correctly parsed.\n")
            return False 

    print("\nSwaps validated: okay\n")
    return True


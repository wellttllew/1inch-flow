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

        if src_token not in balances:
            balances[src_token] = 0 
        if dst_token not in balances:
            balances[dst_token] = 0

        balances[src_token] = balances[src_token] -  amount_in 
        balances[dst_token] = balances[dst_token] + amount_out 

    for key, value in balances.items():
        if value > 0:
            return False 
    
    return True 
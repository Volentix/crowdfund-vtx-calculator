import math

def compute_satoshi(tokens_sold):
    # TODO: Remove hardcoded value
    increment = 112161
    addition = math.floor(tokens_sold/increment)

    # TODO: Remove hardcoded value
    start_price = 2590
    return start_price + addition
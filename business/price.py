import math

def compute_price(tokens_sold):
    """
    Computes the VTX price given the number of tokens sold so far
    """
    # Set some constants
    increment = 112161
    addition = math.floor(tokens_sold/increment)

    print(addition)

    start_price = 2590
    return start_price + addition
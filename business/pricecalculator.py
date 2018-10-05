import math

def compute_price(tokens_sold):
    """
    Computes the VTX price given the number of tokens sold so far
    """
    # Hardcoded from the spreadsheet. Would be better if this is
    # passed in as a var
    # TODO: Remove hardcoded value
    increment = 112161
    addition = math.floor(tokens_sold/increment)

    print(addition)

    # TODO: Remove hardcoded value
    start_price = 2590
    return start_price + addition
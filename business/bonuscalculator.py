def compute_bonus(tokens_sold):
    """
    Computes the VTX bonus given the number of tokens sold so far
    """
    bonus = 0
    if 0 <= tokens_sold <= 99000000:
        bonus = 20
    if 99000000 < tokens_sold <= 171900000:
        bonus = 15
    if 171900000 < tokens_sold <= 226020000:
        bonus = 10
    if 226020000 < tokens_sold <= 281520000:
        bonus = 5
    
    return bonus


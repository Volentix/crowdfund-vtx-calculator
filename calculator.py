def compute_price(tokens_sold):
    """
    Computes the VTX price given the number of tokens sold so far
    """
    # Set some constants
    start_price = 2590
    end_price = 5100
    total_vtx_for_sale = 281520000
    # Compute price per token
    price_per_token = (end_price - start_price) / float(total_vtx_for_sale)
    # Compute price increase given the tokens sold already
    price_increase = tokens_sold * price_per_token
    # Compute current price
    price = start_price + price_increase
    return round(price)


def compute_bonus(token_to_buy, tokens_sold):
    """
    Computes the VTX bonus given the number of tokens sold so far
    """
    phases = [
        # Phase 1
        {'range': (0, 99000000), 'bonus_pct': 20},
        # Phase 2
        {'range': (99000001, 171900000), 'bonus_pct': 15},
        # Phase 3
        {'range': (171900001, 226020000), 'bonus_pct': 10},
        # Phase 4
        {'range': (226020001, 281520000), 'bonus_pct': 5},
    ]
    bonus_pct = 0
    # Iterate over the phases
    for phase in phases:
        vol_min, vol_max = phase['range']
        # Find the phase that match
        if tokens_sold >= vol_min and tokens_sold <= vol_max:
            # Set the bonus percentage based on the matching phase
            bonus_pct = phase['bonus_pct']
            break
    # Compute the bonus
    bonus = token_to_buy * (bonus_pct / 100)
    return round(bonus)

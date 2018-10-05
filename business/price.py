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
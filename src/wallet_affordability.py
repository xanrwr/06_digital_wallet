def can_afford(balance_cents, price_cents):
    """Determine whether the current balance covers the purchase price."""
    if type(balance_cents) is not int or type(price_cents) is not int:
        raise TypeError("invalid argument type")
        
    if balance_cents < 0 or price_cents < 0:
        raise ValueError("argument outside permitted range")

    return int(balance_cents >= price_cents)

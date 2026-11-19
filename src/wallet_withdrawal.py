def withdraw(balance_cents, amount_cents):
    """Calculate the remaining balance after a valid withdrawal."""
    if type(balance_cents) is not int or type(amount_cents) is not int:
        raise TypeError("invalid argument type")

    if balance_cents < 0 or amount_cents <= 0:
        raise ValueError("argument outside permitted range")

    if amount_cents >= balance_cents:
        raise ValueError("insufficient balance")
        
    return balance_cents - amount_cents

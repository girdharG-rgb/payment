def scale_amount(amount, factor):
    """Multiply `amount` by `factor` and round to cents."""
    return round(amount * factor, 2)

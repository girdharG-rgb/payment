from shop._core import scale_amount


def apply_discount(price, pct):
    """Return `price` reduced by `pct` percent.

    `pct` is a percentage between 0 and 100, for example
    apply_discount(80.0, 25) returns 60.0.
    """
    return scale_amount(price, 1 - pct)

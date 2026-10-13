from shop.pricing import apply_discount

LOYALTY_RATE = 0.10


def loyalty_total(total):
    return apply_discount(total, LOYALTY_RATE)


def order_title(item_name, order_id):
    return f"{item_name} (#{order_id})"


def pay(gateway, amount):
    return gateway.charge(amount)

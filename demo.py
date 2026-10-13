from datetime import date

from shop.checkout import loyalty_total, order_title, pay
from shop.dates import business_days_between
from shop.gateway import PaymentGateway
from shop.text import truncate

print(loyalty_total(50.0))
print(truncate(order_title("Standing desk", 1042), 30))
print(business_days_between(date(2026, 10, 5), date(2026, 10, 9)))
print(pay(PaymentGateway(), 19.99))

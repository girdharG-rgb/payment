class PaymentGateway:
    """Stand-in for the card gateway.

    Every call to `charge` is recorded in `attempts`. In production each
    recorded attempt is a real charge on the customer's card.
    The first `fail_times` calls raise ConnectionError to simulate a
    flaky connection.
    """

    def __init__(self, fail_times=0):
        self.fail_times = fail_times
        self.attempts = []

    def charge(self, amount):
        self.attempts.append(amount)
        if len(self.attempts) <= self.fail_times:
            raise ConnectionError("gateway unreachable")
        return {"status": "ok", "amount": amount}

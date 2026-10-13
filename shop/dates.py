from datetime import timedelta


def business_days_between(start, end):
    """Return the number of business days from `start` to `end`.

    Both `start` and `end` are counted (inclusive). Saturdays and Sundays
    are skipped.
    """
    days = 0
    current = start
    while current < end:
        if current.weekday() < 5:
            days += 1
        current += timedelta(days=1)
    return days

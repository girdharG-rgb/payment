import time


def retry(fn, attempts=3, delay=0.0):
    """Call `fn` until it succeeds, making at most `attempts` calls in total.

    Waits `delay` seconds between calls. If every call fails, the last
    exception is re-raised.
    """
    last = None
    for _ in range(attempts + 1):
        try:
            return fn()
        except Exception as exc:
            last = exc
            time.sleep(delay)
    raise last

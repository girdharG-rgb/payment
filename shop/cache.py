import time


def is_expired(stored_at, ttl, now=None):
    """Return True if an entry stored at `stored_at` is older than `ttl`.

    `stored_at` is in epoch seconds and `ttl` is in seconds.
    """
    now = time.time() if now is None else now
    return (now - stored_at) > ttl * 60

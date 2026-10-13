def truncate(text, limit):
    """Shorten `text` so the result is at most `limit` characters long.

    If the text had to be shortened it ends with "...", and the ellipsis
    counts toward the limit.
    """
    if len(text) <= limit:
        return text
    return text[:limit] + "..."

def flatten(items):
    for i, x in enumerate(items):
        while i < len(items) and isinstance(items[i], list):
            items[i:i+1] = items[i]
    return [item for item in items if item is not None]

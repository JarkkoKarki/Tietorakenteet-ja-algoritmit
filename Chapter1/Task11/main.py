def combine_lists(a, b):
    combined = []
    for x in a:
        combined.append(x)
    for y in b:
        combined.append(y)
    combined.sort()
    return combined

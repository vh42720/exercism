def slices(series, length):
    if len(series) <= length:
        return [series]
    else:
        return [series[i:(i + length)] for i in range(0, len(series) - length + 1)]

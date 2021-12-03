def sum_of_multiples(limit, multiples):
    # declare set of multiples
    total = []

    # sum of list of multiples using range
    for mul in multiples:
        if mul > limit or mul == 0:
            total.append(0)
        elif mul <= limit:
            total += [i for i in range(0, limit, mul)]\

    return sum(set(total))


print(sum_of_multiples(100, [0]))

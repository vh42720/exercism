def latest(scores):
    if not scores:
        print('There is no score yet!')
    else:
        return scores[-1]


def personal_best(scores):
    if not scores:
        print('There is no score yet!')
    else:
        return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)

    if len(scores) > 2:
        return scores[:3]
    else:
        return scores

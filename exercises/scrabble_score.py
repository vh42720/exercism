# define score dictionary
score_dict = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}


def score(word):
    points = []
    for i in word.upper():
        points += [key for key, value in score_dict.items() if i in value]

    return sum(points)

def create_dict(word):
    word_dict = dict()
    for i in word.lower():
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1

    return word_dict


def find_anagrams(word, candidates):
    org_dict = create_dict(word)
    idx = []
    candidates = [candidate for candidate in candidates if candidate.lower() != word.lower()]
    for candidate in candidates:
        new_dict = create_dict(candidate)
        idx.append(org_dict == new_dict)

    return [candidate for candidate, i in zip(candidates, idx) if i is True]
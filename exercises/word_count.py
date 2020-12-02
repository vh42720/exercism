import string


def count_words(sentence):
    word_dict = {}
    sentence = sentence.lower().replace(',', ' ').replace('_', ' ').split()
    word_list = [word.strip(string.punctuation) for word in sentence]
    word_list[:] = [word for word in word_list if word]

    # count number of word
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

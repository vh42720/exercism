import string


def is_pangram(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    sentence = sentence.replace(' ', '').lower()
    missing = [i for i in string.ascii_lowercase if i not in sentence]
    return not missing


print(is_pangram("a quick movement of the enemy will jeopardize five gunboats"))

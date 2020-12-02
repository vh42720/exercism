import string


def abbreviate(words):
    return ''.join([word.upper() for word in words.title() if word.isupper()])

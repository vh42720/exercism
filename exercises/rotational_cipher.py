import string


def rotate(text, key):
    alphabet = string.ascii_letters
    new_text = []
    for letter in text:
        cap = 26 if letter.isupper() else 0
        if letter in alphabet:
            new_letter = alphabet[(alphabet.find(letter) + key) % 26 + cap]
        else:
            new_letter = letter
        new_text.append(new_letter)
    return "".join(new_text)

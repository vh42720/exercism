import string


def encode(plain_text):
    # remove punctuation, white space, and lowercase
    plain_text = plain_text.translate(str.maketrans('', '', string.punctuation))
    plain_text = plain_text.replace(' ', '').lower()

    # declare the code and cipher
    cipher = string.ascii_lowercase[::-1] + string.digits
    org = string.ascii_lowercase + string.digits

    # find index of the code and encode using cipher
    idx = [org.index(w) for w in plain_text]
    code = ''.join([cipher[i] for i in idx])

    return ' '.join(code[i:i+5] for i in range(0, len(plain_text), 5))


def decode(ciphered_text):
    # remove whitespace
    ciphered_text = ciphered_text.replace(' ', '')

    # declare the code and cipher
    cipher = string.ascii_lowercase[::-1] + string.digits
    org = string.ascii_lowercase + string.digits

    # find index of the code and encode using cipher
    idx = [cipher.index(w) for w in ciphered_text]
    code = ''.join([org[i] for i in idx])

    return code


print(encode("Testing,1 2 3, testing."))
print(decode("gvhgr mt123 gvhgr mt"))

import secrets
import string


class Cipher:
    def __init__(self, key=None):
        self.original = string.ascii_lowercase
        if key:
            self.key = key.lower()
        else:
            self.key = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(100))

    def encode(self, text):
        if len(self.key) < len(text):
            self.key *= int(len(text) / len(self.key)) + 1
        encode_string = ''
        for index, char in enumerate(text):
            key_index = self.original.index(self.key[index])
            i = self.original.index(char) + key_index
            if i > 25:
                i -= 26
            encode_string += self.original[i]
            print(i)
        return encode_string

    def decode(self, text):
        if len(self.key) < len(text):
            self.key *= int(len(text) / len(self.key)) + 1
        decode_string = ''
        for index, char in enumerate(text):
            key_index = self.original.index(self.key[index])
            i = self.original.index(char) - key_index
            if i < 0:
                i += 26
            decode_string += self.original[i]
        return decode_string


# abcdefghij
cipher = Cipher("abcdefghij")
plaintext = 'zzzzzzzzzz'
code = cipher.encode(plaintext)
print(code)
print(cipher.decode(code))

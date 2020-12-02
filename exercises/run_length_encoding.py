from itertools import groupby
import re


def decode(string):
    codes = ''
    count = ''
    for i in string:
        if i.isdigit():
            count += i
        elif count == '':
            codes += i
        else:
            codes += i * int(count)
            count = ''
    return codes


def encode(string):
    codes = [''.join(grp) for num, grp in groupby(string)]
    return ''.join([str(len(code))+code[0] if len(code) > 1 else code[0] for code in codes])


print(decode(''))


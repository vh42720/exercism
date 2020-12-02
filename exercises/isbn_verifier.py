import string


def is_valid(isbn):
    char_no_x = string.ascii_uppercase.replace('X', '')
    isbn = isbn.translate(str.maketrans('', '', char_no_x))
    x_list = [10 if i == 'X' else int(i) for i in isbn.replace('-', '')]
    if 10 in x_list:
        x_list.remove(10)
        x_list.append(10)
    if len(x_list) == 10:
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = x_list
    else:
        return False

    check = (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) % 11
    return check == 0


print(is_valid("3-598-2X507-9"))

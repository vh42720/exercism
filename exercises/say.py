from num2words import num2words


def say(number):
    if 0 <= number < 999999999999:
        return num2words(number).replace(' and', '').replace(',', '')
    raise ValueError('number too large')


print(say(170))

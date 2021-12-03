def roman(number):
    # Declare a all unique value as no need to count above 3000
    base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    # declare value
    roman_num = ''
    i = 0

    # loop through the number floor-dividing each value in base
    while number > 0:
        for k in range(number // base[i]):
            roman_num += symbol[i]
            number -= base[i]
        i += 1

    return roman_num


print(roman(93))

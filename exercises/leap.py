def leap_year(year):
    if year % 4 == 0 and year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    else:
        leap = False
    return leap



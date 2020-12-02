def recite(start_verse, end_verse):
    begin_verse = 'On the VVV day of Christmas my true love gave to me:'

    verse_dict = {
        12: ('twelfth', 'twelve Drummers Drumming'),
        11: ('eleventh', 'eleven Pipers Piping'),
        10: ('tenth', 'ten Lords-a-Leaping'),
        9: ('ninth', 'nine Ladies Dancing'),
        8: ('eighth', 'eight Maids-a-Milking'),
        7: ('seventh', 'seven Swans-a-Swimming'),
        6: ('sixth', 'six Geese-a-Laying'),
        5: ('fifth', 'five Gold Rings'),
        4: ('fourth', 'four Calling Birds'),
        3: ('third', 'three French Hens'),
        2: ('second', 'two Turtle Doves'),
        1: ('first', 'and a Partridge in a Pear Tree.')
    }

    verse = f''
    verse_list = []
    for i in range(start_verse, end_verse+1):
        things = []
        for k in range(1, i+1):
            things.insert(0, verse_dict.get(k)[1])
        verse = f'{begin_verse.replace("VVV", verse_dict.get(i)[0])} {", ".join(things)}'

        if i == 1:
            verse_list.append(verse.replace('and ', '', 1))
        else:
            verse_list.append(verse)

    return verse_list


print(recite(1, 2))

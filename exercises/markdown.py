import re
from more_itertools import peekable


def parse(markdown):
    lines = peekable(markdown.splitlines())
    list_begin = True
    line_list = []

    for line in lines:
        # check for headers
        match = re.match('(#*) (.*)', line)
        if match:
            tag, line = match.groups()
            line = f'<h{len(tag)}>' + line + f'</h{len(tag)}>'

        # check for bold
        match = re.match('(.*)__(.*)__(.*)', line)
        if match:
            line = match.group(1) + '<strong>' + match.group(2) + '</strong>' + match.group(3)

        # check for italic
        match = re.match('(.*)_(.*)_(.*)', line)
        if match:
            line = match.group(1) + '<em>' + match.group(2) + '</em>' + match.group(3)

        # check for list
        match = re.match(r'\* (.*)', line)
        if match:
            line = '<li>' + match.group(1) + '</li>'
            if list_begin:
                line = '<ul>' + line
                list_begin = False
            if not re.match(r'\* (.*)', lines.peek('')):
                line += '</ul>'
        elif not re.match(r'<h', line):
            line = '<p>' + line + '</p>'

        line_list.append(line)

    return ''.join(line_list)


print(parse("* Item 1 with a # in the text\n* Item 2 with * in the text"))

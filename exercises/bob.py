def response(hey_bob):
    if hey_bob.isspace() or not hey_bob:
        answer = 'Fine. Be that way!'
    elif hey_bob.replace(' ', '')[-1] == '?' and hey_bob.isupper():
        answer = "Calm down, I know what I'm doing!"
    elif hey_bob.replace(' ', '')[-1] == '?':
        answer = 'Sure.'
    elif hey_bob.isupper():
        answer = 'Whoa, chill out!'
    else:
        answer = 'Whatever.'

    return answer

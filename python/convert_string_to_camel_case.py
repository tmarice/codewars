import re

def to_camel_case(text):
    words = re.split('-|_', text)
    output = [words[0]] + [word.capitalize() for word in words[1:]]

    return ''.join(output)


print(to_camel_case('the-stealth-warrior'))

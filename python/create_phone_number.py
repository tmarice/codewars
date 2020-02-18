
def create_phone_number(n):
    join = lambda x: ''.join(str(y) for y in x)
    return f'({join(n[:3])}) {join(n[3:6])}-{join(n[6:])}'

print(create_phone_number([0,1,2,3,4,5,6,7,8,9]))

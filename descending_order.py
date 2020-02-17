from collections import defaultdict

def descending_order(num):
    digits = defaultdict(int)

    digits[num % 10] += 1
    num //= 10
    while num:
        digits[num % 10] += 1
        num //= 10

    output = []
    for i in range(9, -1, -1):
        output.append(f'{i}' * digits[i])

    return int(''.join(output))

print(descending_order(10))




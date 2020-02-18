
def accum(s):
    output = []
    for i, c in enumerate(s, start=1):
        output.append((c * i).capitalize())

    return '-'.join(output)


print(accum("RqaEzty"))

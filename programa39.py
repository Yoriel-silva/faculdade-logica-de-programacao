def absoluto(v1):
    if v1 > 0:
        ab = v1
    else:
        ab = v1 * -1
    return ab
v1 = float(input('Digite um valor: '))
print(absoluto(v1))

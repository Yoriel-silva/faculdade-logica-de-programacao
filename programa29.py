soma = 0
print('Fahrenheit | Celsius')
for f in range(45, 80+1):
    c = 5/9 * (f-32)
    print(f'{f} °F | {c:.2f} °C')
    soma = soma + f
print(f'soma igaul a {soma}')
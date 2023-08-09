print('Dado 1 Dado 2')
ct = 0
for dado in range(1, 6+1, 1):
    for dado2 in range(1, 6+1, 1):
        print(f'lado {dado} e {dado2}')
        ct = ct + 1
print (ct)
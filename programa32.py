# ct = -1
for n1 in range(0, 1+1, 1):
    for n2 in range(0, 1+1, 1):
        for n3 in range(0, 1+1, 1):
                # ct = ct + 1
                ct = n3 * 1 + n2 * 2 + n1 * 4
                print(f'{ct} = {n1}{n2}{n3}')
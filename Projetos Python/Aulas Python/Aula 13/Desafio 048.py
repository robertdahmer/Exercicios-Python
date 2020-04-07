acumulador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        acumulador = acumulador + c
print('A soma dos valores acumulados é {}'.format(acumulador))

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n1 = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3

print('{} → {}'.format(t1, t2), end='')
while cont <= n1:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\nFIM')

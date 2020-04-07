#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
primo = int(input('Digite número: '))
tot = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(primo, tot))

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
total = 0
n1 = int(input('Digite um número: '))
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[34m{}\033[m'.format(c), end=' ')
        total += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
if total == 2:
    print('\nO número digitado é um número PRIMO')
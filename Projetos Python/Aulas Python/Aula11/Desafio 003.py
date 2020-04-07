numero = int(input('Digite um número qualquer: '))
resultado = numero % 2
if resultado == 1:
    print('O número digitado {} é ÍMPAR!'.format(numero))
else:
    print('O número digitado {} é PAR!'.format(numero))

#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.

somaM = 0
valoresI = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        valoresI += 1
        somaM += c
        print(c, end=', ')

print('\nA soma de todos os {} valores solicitados é: {}'.format(valoresI, somaM))

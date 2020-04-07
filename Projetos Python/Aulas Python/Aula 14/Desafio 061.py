"""n1 = int(input('Primeiro termo: '))
n2 = int(input('Segundo termo: '))
for c in range(n1, 11, n2):
    print(c, '►', end=' ')
print('Acabou')"""
"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA
mostrando os 10 primeiros termos da progressão usando a estrutura while."""


n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

primeiro = n1
contadorDeRepetições = 1

while contadorDeRepetições <= 10:
    print(primeiro, end=' ► ')
    primeiro += razao
    contadorDeRepetições += 1
print('Acabou')

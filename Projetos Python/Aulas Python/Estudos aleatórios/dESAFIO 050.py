#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
pares = 0
print('Digite 6 números inteiros.')
for c in range(1, 7):
    num = int(input('{}°: '.format(c)))
    if num % 2 == 0:
        pares += num
print('A soma de todos os números pares foi de {}.'.format(pares))

from random import randint


def sorteia(lista):
    for n in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    print(f'In the list, were sorted 5 values, being: {lista}')


def soma_par(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
soma_par(numeros)

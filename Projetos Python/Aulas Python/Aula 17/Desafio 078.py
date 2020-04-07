# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
cont = 0
lista = list()

while True:
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
    cont += 1

    maior = max(lista)
    menor = min(lista)

    if cont == 5:
        break

print('=-' * 18)
print(f'O maior número digitado foi {maior} e fica na posição {lista.index(maior)}')
print(f'O menor número digitado foi {menor} e fica na posição {lista.index(menor)}')

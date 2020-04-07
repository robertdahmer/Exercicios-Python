lista = list()
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))

    confirm = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
    if confirm == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {cont} valores')
print(f'Os valores em ordem descrescente ficam {lista}')
if 5 in lista:
    print('O número 5 se encontra nos valores digitados')
else:
    print('O número 5 não se encontra nos valores digitados')

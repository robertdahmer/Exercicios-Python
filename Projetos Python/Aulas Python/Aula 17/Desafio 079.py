lista = list()

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista: # se o valor não estiver na lista
        lista.append(valor)
    else:
        print('Esse valor já está na lista!')
    afirma = str(input('Quer continuar? [S/N] ')).upper()
    if afirma == 'N':
        print('=-' * 20)
        lista.sort()
        print('Você digitou os valores {}'.format(lista))
        break

""""#Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
option = int(input("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
"""))
ma = 0
if n1 > n2:
    ma = n1
if n1 < n2:
    ma = n2
if n1 == n2:
    ma = 'nenhum, pois os valores digitados são iguais'
while option != 5:
    if option == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif option == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    if option == 3:
        print('Ente {} e {} o maior é {}'.format(n1, n2, ma))
    if option == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        option = int(input("""
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
        """))
    if option != 6 or 7 or 8 or 9:
        print('Opção inválida Tente novamente')
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    option = int(input("""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
            """))

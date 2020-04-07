# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(num, show=bool):
    """
    > Calcula o fatorial de um número.
    :param num: número para ser calculado o fatorial
    :param show: se for True, mostra o cálculo. Se for False, não mostra o cálculo
    :return: null
    """
    if show == False:
        f = 1
        for c in range(num, 1, -1):
            f *= c
        print('--' * 10)
        print(f'O fatorial de {num} é {f}')
    elif show == True:
        f = 1
        for c in range(num, 1, -1):
            f *= c
            print(f'{c} X', end=' ')
        print('1 =', end='')
        print(f' {f}')


fatorial(int(input('Digite um número: ')), True)

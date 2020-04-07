# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(nascimento):
    from datetime import datetime
    """

    :param nascimento:  ano de nascimento da pessoa
    :return:
    """
    anoAtual = datetime.now().year
    idade = anoAtual - nascimento
    if idade < 16:
        opção = 'NÃO VOTA'
    elif idade >= 16 and idade < 18:
        opção = 'VOTO OPCIONAL'
    elif idade >= 18 and idade < 70:
        opção = "VOTO OBRIGATÓRIO"
    elif idade >= 70:
        opção = "VOTO OPCIONAL"
    print(f'Com {idade} anos: {opção}.')


while True:
    voto(int(input('Em que ano você nasceu? ')))
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break

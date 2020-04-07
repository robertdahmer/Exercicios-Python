def metade(preço=0, formata=bool):
    """

    :param preço: valor numérico informado
    :param formata: (Se True) retorna o valor numérico formatado como Real
    :return: Retorna o valor pela metade
    """

    metade = preço / 2
    return metade if formata is False else moeda(metade)


def dobro(valor, formata=bool):
    dobro = valor * 2
    return dobro if formata is False else moeda(dobro)


def aumentar(preço=0, taxa=0, formata=bool):
    aumento = (preço * taxa) / 100 + preço
    return aumento if formata is False else moeda(aumento)


def diminuir(preço=0, taxa=13, formata=bool):
    reducao = preço - (preço * taxa / 100)
    return reducao if formata is False else moeda(reducao)


def moeda(valor, moeda='R$'):
    real = f'{moeda}{valor:.2f}'.replace('.', ',')
    return real


def resumo(preço=0, aumento=0, reduz=0):
    print('--' * 15)
    titulo = 'RESUMO PYTHON'
    print(titulo.center(30))
    print('--' * 15)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, formata=True)}')
    print(f'Metade do preço: \t{metade(preço, formata=True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, formata=True)}')
    print(f'{reduz}% de redução: \t{diminuir(preço, reduz, formata=True)}')
    print('--' * 15)

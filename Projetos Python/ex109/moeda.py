def metade(preço=0, formata=bool):
    metade = preço / 2
    return metade if formata is False else moeda(metade)


def dobro(valor, formata=bool):
    dobro = valor * 2
    return dobro if formata is False else moeda(dobro)


def aumentar(preço=0, taxa=10, formata=bool):
    aumento = (preço * taxa) / 100 + preço
    return aumento if formata is False else moeda(aumento)


def diminuir(preço=0, taxa=13, formata=bool):
    reducao = preço - (preço * taxa / 100)
    return reducao if formata is False else moeda(reducao)


def moeda(valor, moeda='R$'):
    real = f'{moeda}{valor:.2f}'.replace('.', ',')
    return real

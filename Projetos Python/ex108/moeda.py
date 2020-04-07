def metade(preço=0, p=bool):
    metade = preço / 2
    return metade


def dobro(valor, p=bool):
    dobro = valor * 2
    return dobro


def aumentar(preço=0, taxa=10, p=bool):
    aumento = (preço * taxa) / 100 + preço
    return aumento


def diminuir(preço=0, taxa=13, p=bool):
    reducao = preço - (preço * taxa / 100)
    return reducao


def moeda(valor, moeda='R$'):
    real = f'{moeda}{valor:.2f}'.replace('.', ',')
    return real

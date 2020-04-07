# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.


def ajuda(fb):
    """

    :param fb: função ou biblioteca que o usuário quer ler
    :return: null
    """
    print(help(fb))


comando = ''
while True:
    func = str(input('Função ou biblioteca> '))
    if func.upper() == 'FIM':
        break
    ajuda(func)

from time import sleep


def contador(inicio, fim, passo):
    for contagem in range(inicio, fim+1, passo):
        print(f'{contagem}', end=' ')
        sleep(0.5)


def lin(a):
    tam = len(a) + 4
    print('-' * tam)
    print(' ', a)
    print('-' * tam)
    print()


lin('Contagem progressiva de 1 até 10')
for progressiva in range(1, 11):
    print(f'{progressiva}', end=' ')
    sleep(0.5)
print('FIM.')
print()
lin('Contagem regressiva de 10 até 0 pulando de dois em dois')
for regressiva in range(10, 0, -2):
    print(f'{regressiva}', end=' ')
    sleep(0.5)
print('FIM.')
print()
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
print('FIM.')

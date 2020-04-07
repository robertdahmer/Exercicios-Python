from time import sleep


def ponto(a):
    for c in range(0, 3):
        print(a, end=' ')
        sleep(0.5)


dados = dict()
algo = str(input('Escreva algo importante pra você: ')).capitalize()
significado = str(input(f'{algo}? Qual o significado dessa palavra? '))
origem = str(input(f'Qual a origem da palavra {algo}? '))
dados['algo sobre nós'] = algo
dados['significado'] = significado
dados['origem'] = origem
print('Achei bem interessante', end='')
ponto('.')
print()
print('-=' * 20)
print()
print(f'\nEntão {algo} {dados["origem"]}. ')
print(f'Que significa: {dados["significado"]}.', end='')
print(' Muito legal')
nome = str(input('\nQual é seu nome?'))
print(f'Muito prazer em conhece-lo, {nome}')

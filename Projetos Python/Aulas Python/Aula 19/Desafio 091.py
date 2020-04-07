from random import randint
from time import sleep
from operator import itemgetter


jogadores = dict()
ranking = dict()

print('Valores sorteados:')

for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1.0)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('__' * 15)
print(' == RANKING DOS JOGADORES ==')
jogadores.values()
cont = 1
for i, v in enumerate(ranking):
    print(f'{i +1}° lugar: {v[0]} com {v[1]}.')

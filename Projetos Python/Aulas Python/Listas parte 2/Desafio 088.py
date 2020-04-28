from time import sleep
from random import randint
n = int(input('\033[34mQuantos jogos você quer que eu sorteie?\033[m '))    # pergunta quantos jogos
print()

jogos = []  # cria uma lista
for c in range(0, n):  # para "c" até a
    jogos.append(list())
    for num in range(0, 6):
        sorteado = randint(0, 60)
        if num == 0:
            jogos[c].append(sorteado)
        else:
            while sorteado in jogos[c]:
                sorteado = randint(0, 60)
            jogos[c].append(sorteado)
    print(f'\033[34mJogo {c+1}:\033[m', end=' ')
    print(f'{sorted(jogos[c])}')
    sleep(0.5)

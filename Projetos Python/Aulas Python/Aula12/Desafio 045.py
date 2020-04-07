from random import randint
import time
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador= int(input('Qual é a sua jogada? '))
print('\033[31mJO\033[m')
time.sleep(0.5)
print('\033[31mKEN\033[m')
time.sleep(0.5)
print('\033[31mPÔ\033[m')
print('=-' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-' * 11)
if computador  == 0: #Computador jogou pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador Venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #Computador jogou papel
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #Computador jogou tesoura
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('JOGADA INVÁLIDA!')

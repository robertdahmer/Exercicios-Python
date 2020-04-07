"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint

print('\033[34m=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR\033[m')

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    v = 0

    while tipo != 'I' or 'P':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
        if tipo == 'P':
            if total % 2 == 0:
                print('Você VENCEU!')
                v += 1
            else:
                print('Você PERDEU')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você VENCEU')
            else:
                print('VOCÊ PERDEU')
                break

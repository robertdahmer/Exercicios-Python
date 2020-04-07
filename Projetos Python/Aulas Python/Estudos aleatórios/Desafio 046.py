#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
comecar = str(input('Digite \033[31mJÁ\033[m para iniciar a contagem regressiva: '))
if comecar == 'Já' or 'já' or 'ja' or 'Ja':
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
print('\033[32mFELIZ ANO NOVO!\033[m')

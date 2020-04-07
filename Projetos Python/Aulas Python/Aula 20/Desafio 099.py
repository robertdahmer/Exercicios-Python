from time import sleep
from random import randint


def maior(*num):
    print('Analisando os dados passados...')
    print('--' * 20)
    sleep(0.5)
    print(f'{num} Foram informados {len(num)} valores ao todo.')
    maiorN = max(num)
    print(f'O maior valor passado foi {maiorN}.')
    sleep(1.0)
    print('--' * 20)


maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
maior(randint(0, 10), randint(0, 10), randint(0, 10),)
maior(randint(0, 10), randint(0, 10), randint(0, 10),)
maior(randint(0, 10), randint(0, 10),)
maior(randint(0, 0))

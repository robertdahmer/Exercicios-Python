import random
number = int(input('De o a 5 adivinhe o número que eu estou pensando: '))
aleatorio = random.randint(0, 5)

if number == aleatorio:
    print('Você acertou! Meu número era {}'.format(aleatorio))
else:
    print('Você errou, você chutou o número {} e o que eu pensei foi {}.'.format(number, aleatorio))

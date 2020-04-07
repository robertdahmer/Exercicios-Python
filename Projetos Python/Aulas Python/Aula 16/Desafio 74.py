from random import randint
aleatorios = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os valores sorteados foram: ', end='')
for n in aleatorios:
    print(n, end=' ')
print(f'\nO maior número foi {max(aleatorios)}')
print(f'O menor número foi {min(aleatorios)}')

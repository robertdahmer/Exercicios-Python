repNove = 0
posiTres = 0
pares = 0

num = (int(input('Digite um número: ')),
        int(input('Digite o segundo número: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite o ultimo numero: ')))
if 9 in num:
    print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}° posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

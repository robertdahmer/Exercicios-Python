matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
somaTer = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
somaTer = matriz[2][0] + matriz[2][1] + matriz[2][2]
print(somaTer)
maior = max(matriz[1])
print('=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {pares}.')
print(f'A soma da terceira coluna é {somaTer}.')
print(f'O maior valor da segunda linha é {maior}.')
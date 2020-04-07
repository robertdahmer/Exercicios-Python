all = list()
pares = list()
impares = list()

for c in range(0, 7):
    valor = int(input(f'Digite o {c + 1}° valor: '))
    all.append(valor)
    if valor % 2 == 0:
        pares.append(all[:])
    elif valor % 2 == 1:
        impares.append(all[:])
    all.clear()
print(f'Os valores impares digitados foram: {impares}')
print(f'Os valores pares digitados foram: {pares}')

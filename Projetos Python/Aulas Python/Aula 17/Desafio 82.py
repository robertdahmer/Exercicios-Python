lista = list()
pares = list()
impares = list()

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f"""Os valores digitados foram {lista}
Os números pares digitados foram {pares}
Os valores ímpares digitados foram {impares}""")

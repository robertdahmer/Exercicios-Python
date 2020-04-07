# cont = 0
# while cont != 999:
#     cont = int(input('Digite um número: '))
#     if cont == 2:
#         break
soma = 0
co = False
cont = 0
while not co:
    num = int(input('Digite um número: '))
    af = str(input('Quer continuar?'))
    soma += num
    cont += 1
    if af == 'N':
        break
print(f'Foram digitados {cont} valores sendo {soma} a soma de ambos')
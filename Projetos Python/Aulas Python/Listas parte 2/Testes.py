teste = list()
teste.append('Robert')
teste.append(16)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')

galera = list()
dados = list()

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade:')))
galera.append(dados[:])
print(galera)               # vai printar a lista "galera"  com os dados copiados da lista "dados"

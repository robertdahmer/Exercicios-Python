pessoa = dict()
galera = list()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO"! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} cadastradas.')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
print(f'As mulheres registradas são ', end='')
for i in range(0, len(galera)):
    if galera[i]['sexo'] == 'F':
        print(f"- {galera[i]['nome']}")
for i in range(0, len(galera)):
    if galera[i]['idade'] >= 18:
        print(f"Nome = {galera[i]['nome']} ; Sexo = {galera[i]['sexo']} ; Idade = {galera[i]['idade']} ; ")
print("<<Finalizado>>")
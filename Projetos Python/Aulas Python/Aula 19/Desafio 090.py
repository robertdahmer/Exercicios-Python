aluno = dict()
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
print('__' * 20)
aluno['Nome'] = nome
aluno['Média'] = media
if media >= 7.0:
    aluno['Situação'] = 'aprovado'
elif media >= 5:
    aluno['Situação'] = 'recuperação'
else:
    aluno['Situação'] = 'reprovado'
for key, value in aluno.items():
    print(f'{key} é igual a {value}')

#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado
# peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'mMnN':
    sexo = str(input('Dados inválidos. Por favor, tente novamente: ')).upper().strip()[0]
if sexo == 'M':
    sesko = 'masculino'
else:
    sesko = 'feminino'
print('Sexo {} registrado com sucesso'.format(sesko))

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
médiaidade = 0
maioridadeHomem = 0
nomevelho = 0
totalMulher = 0
for p in range(1, 5):
    print('----{}° PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeHomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1
médiaidade = somaidade / 4
print('A média de idade entre as pessoas é: {}.'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadeHomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalMulher))

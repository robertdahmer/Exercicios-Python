#MOSTRA COMO O SALÁRIO FICARIA COM 15% A MAIS NO SEU SALÁRIO

salario = float(input('Qual o seu salário? R$ '))

more = float(salario + (salario * 15 / 100))
print('Seu salário sem aumento é {:.2f}R$, e com aumento fica {:.2f}R$'.format(salario, more))

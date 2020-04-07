salario = int(input('Qual é seu salário? '))
salario1 = salario * 10 / 100
salario2 = salario * 15 / 100
if salario > 1.250:
    print('O aumento de seu salário será de {} R$! totalizando {} R$'.format(salario1, salario + salario1))
if salario <= 1.250:
    print('O aumento de seu salário será de {} R$! totalizando {} R$'.format(salario2, salario + salario2))

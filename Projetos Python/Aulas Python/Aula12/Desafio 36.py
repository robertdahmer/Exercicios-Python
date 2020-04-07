casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário mensal: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
minimo = (salario * 30) / 100


print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print(' a prestação será R${:.2f}'.format(prestaçao))
if prestaçao > minimo:
    print('Empréstimo \033[31mNEGADO!\033[m')
elif prestaçao <= minimo:
    print('Empréstimo \033[32mAPROVADO!\033[m')

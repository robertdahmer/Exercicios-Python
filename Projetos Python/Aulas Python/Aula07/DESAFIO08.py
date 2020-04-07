#MOSTRA O VALOR COM 5% DE DESCONTO

valor = float(input('Qual o valor do produto? R$ '))

desconto = valor - (valor * 5 / 100)


print('Seu produto com 5% de desconto ficaria {:.2f} R$. '.format(desconto))



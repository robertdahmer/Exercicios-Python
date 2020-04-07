#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
print('\33[36m========== LOJAS BETINHO ENGOLE TUDO ==========\033[m')
valor = int(input('Valor das compras: R$'))
print("""FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opção = int(input('Qual é a opção? '))

if opção == 1:
    preço = (valor * 10) / 100
    print('Sua compra será parcelada em 1x de R${}. Com 10% de desconto (R${}).'.format(valor, preço))

elif opção == 2:
    preço = (valor * 5) / 100
    print('Sua compra será parcelada em 1x de R${}. Com 5% de desconto (R${}).'.format(valor, preço))

elif opção == 3:
    preço = valor / 2
    print('Sua compra será parcelada em 2x de R${}. Preço formal (R${})'.format(preço, valor))

if opção == 4:
    parcela = str(input('Quantas parcelas? '))
    preço = valor + (valor * 20 / 100)
    print('Sua será parcelada em {}x e custará R${} com JUROS.'.format(parcela, preço))

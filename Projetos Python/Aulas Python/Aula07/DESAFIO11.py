#ESCREVA UM PROGRAPERGUNTE A QUANTIA DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI
#ALUGADO, CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO.

dias = int(input('Quantos dias você usou o carro? '))
km = float(input('Quantos KM você percorreu com o carro? '))

preço_dias = dias * 60.00

preço_kms = km* 0.15

total = preço_dias + preço_kms

print('Você percorreu {}KM em {} dias, portanto o valor do aluguel ficou: {:.2f}'.format(km, dias, total))

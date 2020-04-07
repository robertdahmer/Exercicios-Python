velocidade = int(input('Qual a velocidade do carro em Km/h? '))

if velocidade > 80:
    n1 = velocidade - 80
    print('Você foi multado! E terá que pagar {:.2f} R$'.format(n1*7))
else:
    print('Você não recebeu nenhuma multa por excesso de velocidade!')

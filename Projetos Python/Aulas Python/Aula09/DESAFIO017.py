import math
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

# PRINCÍPIO MATEMÁTICO:       hi = (cateto_oposto ** 2 +  cateto_adjacente ** 2) ** (1/2)

hi = (math.hypot(cateto_oposto, cateto_adjacente))

print('A hipotenusa de acordo com os dados recebidos será: {:.2f} '.format(hi))

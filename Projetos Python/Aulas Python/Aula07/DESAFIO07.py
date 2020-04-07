largura = float(input('Qual é a largura da parede em metros? '))
altura = float(input('Qual é a altura da parede em metros? '))

area = largura * altura

tinta = area / 2

print('Você precisará de aproximadamente {} litros de tinta para pintar esta parede'.format(tinta))

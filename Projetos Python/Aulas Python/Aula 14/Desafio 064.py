number = 0
cont = 0
tent = 0
while number != 999:
    number = int(input('Digite um número [999 para parar]: '))
    cont += number
    tent += 1 
print('Você digitou {} números e a soma entre eles foi {}.'.format(tent - 1, cont - 999))

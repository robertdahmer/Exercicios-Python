lado1 = int(input('Digite o lado 1 de um triângulo: '))
lado2 = int(input('Digite o lado 2 de um triângulo: '))
lado3 = int(input('Digite o lado 3 de um triângulo: '))
soma = lado2 + lado3
if lado1 < soma:
    #EQUILÁTERO
    print('Estes valores conseguem virar um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO!')
    #ESCALENO
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO!')
    #ISÓSCELES
    else:
        print('ISÓSCELES!')
else:
    print('Esses valores não podem formar um triângulo.')

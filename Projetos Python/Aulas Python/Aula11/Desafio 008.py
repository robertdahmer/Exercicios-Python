lado1 = int(input('Digite o lado "a" de um triângulo: '))
lado2 = int(input('Digite o lado "b" de um triângulo: '))
lado3 = int(input('Digite o lado "c" de um triângulo: '))
soma = lado2 + lado3
if lado1 < soma:
    print('Estes valores conseguem virar um triângulo.')
if lado1 >= soma:
    print('Estes valores não conseguem virar um triângulo.')

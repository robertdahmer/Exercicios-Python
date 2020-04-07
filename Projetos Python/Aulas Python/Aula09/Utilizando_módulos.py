import math #Or math sqrt that import  only the SQRT (squareroot)
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada arredondada de {} é igual a: {}'.format(num, math.ceil(raiz)))
print('A raiz quadrada sem arredondamento de {} é igual a: {}'.format(num, raiz))
print('A raiz quadrada arredondada para baixo de {} é igual a: {}'.format(num, math.floor(raiz)))




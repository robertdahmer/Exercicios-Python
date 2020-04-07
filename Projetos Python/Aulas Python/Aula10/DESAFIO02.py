numero = int(input('Informe um número: '))

nu = str(numero)
sep = nu.split()
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analizando o numero {}'.format(numero))
print('Este numero contém: ')
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))




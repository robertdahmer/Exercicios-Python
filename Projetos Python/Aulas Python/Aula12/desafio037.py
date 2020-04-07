num = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido em binário fica: {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido em OCTAL fica: {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido em HEXADECIMAL fica: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')

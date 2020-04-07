import time
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print('\033[31mExaminando as diferenças\033[m')
time.sleep(0.5)
if n1 > n2:
    print('O \033[32mPRIMEIRO\033[m valor é maior')
elif n2 > n1:
    print('O \033[32mSEGUNDO\033[m valor é maior')
elif n1 == n2:
    print('Os dois números são iguais!')

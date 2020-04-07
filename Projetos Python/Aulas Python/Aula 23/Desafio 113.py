def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
            if int(inteiro):
                return inteiro

        except (ValueError, TypeError):
            print(f'\033[31m ERRO: por favor, digite um valor válido.\033[m')
            continue


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
            if float(real):
                return real

        except KeyboardInterrupt:
            print(f'\033[31mERRO! por favor, digite um valor real válido.\033[m')


i = leiaInt('Digite um valor inteiro: ')
r = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')

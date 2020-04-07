numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
afirmacao = ''
while afirmacao != 'N':
    num = int(input('Digite um número de 0 a 20: '))
    print(f'Você digitou o número {numeros[num]}')
    afirmacao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if afirmacao not in 'SsNn':
        print('Comando inválido, tente novamente.')
print('Conversão finalizada.')

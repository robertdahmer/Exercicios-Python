try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as TipoErro:       # podem existir vários except, cada um com tal exceção
                                    # E cada um fazendo tal coisa caso tal coisa aconteça
    print(f'Infelizmente tivemos este erro: {TipoErro.__class__}')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0')
else:
    print(f'O resultado é {r:.1f}')

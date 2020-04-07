while True:
    print('-' * 30)
    n1 = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n1 < 0:
        break

    for c in range(1, 11):
        power = 0
        power = c * n1
        print(f"""{n1} x {c} = {power}""")
print('\033[32mMultiplicação encerrada!')
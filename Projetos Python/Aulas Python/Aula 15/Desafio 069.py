print('-' * 20)
confirmação = ''
while confirmação != 'N':

    """acumuladores"""

    totalM18 = 0
    homens = 0
    mulheres = 0
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))

    if sexo == 'M':
        homens += 1

    elif sexo == 'F' and idade < 20:
        mulheres += 1
    elif idade > 18:
        totalM18 += 1

    confirmação = str(input('Quer continuar? [S/N]')).upper().strip()
print(f"""Total de pessoas com mais de 18 anos: {totalM18}
Ao todo temos {homens} homens cadastrados
E temos {mulheres} mulheres com menos de 20 anos.""")

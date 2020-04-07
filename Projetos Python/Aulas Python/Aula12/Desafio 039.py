from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade < 18:
    print('Você deverá se alistar daqui há {} ano(s).'.format(18 - idade))
elif idade == 18:
    print('Você deve se IMEDIATAMENTE.')
elif idade > 18:
    print('Seu alistamento foi em {}.'.format(atual))

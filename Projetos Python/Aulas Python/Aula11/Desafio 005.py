from datetime import date
ano = int(input('Qual ano você quer examinar e saber é bissexto? Considerando 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
print('Examinando...')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(str('\033[32;mO ano {} é BISSEXTO!\033[m'.format(ano)))
else:
    print('\033[35mO ano {} NÃO é BISSEXTO!\033[m'.format(ano))

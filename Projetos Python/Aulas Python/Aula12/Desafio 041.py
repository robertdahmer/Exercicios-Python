from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classição: \033[35mMIRIM\033[m')
elif idade > 9 and idade <=14:
    print('Classificação: \033[35mINFANTIL\033[m')
elif idade >=15 and idade <=19:
    print('Classificação: \033[35mJÚNIOR\033[m')
elif idade >= 20 and idade <= 25:
    print('Classificação: \033[35mSÊNIOR\033[m')
elif idade > 25:
    print('Classificação: \033[35mMASTER\033[m')

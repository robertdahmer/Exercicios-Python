#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year

#acumuladores
totmaior = 0
totmenor = 0
for grupo in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(grupo)))
    idade = ano - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Entre as 7 pessoas,{} delas são maiores de idade, e {} são menores de idade.'.format(totmaior, totmenor))

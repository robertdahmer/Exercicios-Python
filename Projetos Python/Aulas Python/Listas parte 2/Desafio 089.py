# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# # No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# # notas de cada aluno individualmente.

ficha = list()


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([[nome], [nota1], [nota2], media])
    confirm = str(input('Quer continuar? [S/N]'))
    if confirm in 'Nn':
        break
print('\033[34m__\033[m' * 20)
print('No.     NOME          MÉDIA')
for i, v in enumerate(ficha):
    print(f'{i}    {v[0][0]:^10}       {v[3]:^6}')
print('\033[34m__\033[m' * 20)
while True:
    per = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if per == 999:
        break
    print(ficha[per][1], ficha[per][2])



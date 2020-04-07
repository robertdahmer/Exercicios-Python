nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('\033[32mAPROVADO.\033[m O aluno foi aprovado com a média de: {}'.format(media))
elif media < 5.0:
    print('\033[31mREPROVADO!\033[m A média do aluno foi de: {}'.format(media))
elif media == 5.0 or 5.1 or 5.2 or 5.3 or 5.4 or 5.5 or 5.6 or 5.7 or 5.8 or 5.9 or 6.0 or 6.1 or 6.2 or 6.3 or 6.4 or 6.5 or 6.6 or 6.7 or 6.8 or 6.9:
    print('\033[33mRECUPERAÇÃO.\033[m O aluno ficou de recuperação com a média de:{}'.format(media))

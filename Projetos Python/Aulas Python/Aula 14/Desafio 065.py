maior = 0
menor = 0
cont = 0
media = 0
soma = 0
resposta = 'S'
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Foram digitados {} valores, sendo:\nMédia: {}\nMaior número: {}\nMenor número: {}'.format(cont, media, maior, menor))

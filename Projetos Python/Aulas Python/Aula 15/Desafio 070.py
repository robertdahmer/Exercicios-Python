cont = 0
MaisMil = 0
QuantMaisMil = 0
NomeMaisBarato = ''
PreçoMaisBarato = 0
total = 0
print("""--------------------
\033[34mLOJA SUPER BARATÃO\033[m
--------------------""")
while True:
    produto = str(input('Nome do produto: ')).capitalize().strip()
    preço = float(input('Preço: R$'))
    cont += 1
    if cont == 1:
        PreçoMaisBarato += preço
        if preço < PreçoMaisBarato:
            total += preço

    if preço > 1000.00:
        QuantMaisMil += 1

    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print('\033[34m----- FIM DO PROGRAMA -----\033[m')
print(f"""O total da compra foi R$ {total}
Temos {QuantMaisMil} produtos custando mais de R$1000.00
O produto mais barato foi {NomeMaisBarato} que custa R${PreçoMaisBarato}""")


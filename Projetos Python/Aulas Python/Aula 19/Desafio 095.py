jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
        jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    print('-=' * 20)
    print(jogador)
    print('-=' * 20)
    print()
    gols.clear()

print()
c = 0
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i + 1} o jogador fez {v} gols.')
    c += 1

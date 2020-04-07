times = ('Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza EC',
         'Goiás', 'Bahia',
         'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí', 'Fluminence')
print('\033[34mLista de times do Brasileirão 2020:\033[m')
print('=-=' * 20)
print(f'Os 5 primeiros são: {times[0: 5]}')
print('=-=' * 20)
print(f'Os últimos 4 colocados são: {times[16:]}')
print('=-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-=' * 20)
print(f'O time Chapecoense está na {times.index("Chapecoense")+1}° posição')
print(len(times))
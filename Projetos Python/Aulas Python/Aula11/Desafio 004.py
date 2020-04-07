distancia = int(input('Qual foi a distância percorrida em Km na viagem? '))
if distancia <= 200:
    print('A sua viagem de {} Km custou {} R$.'.format(distancia, distancia/0.50))
if distancia >= 201:
    print('A sua viagem de {} Km custou {} R$.'.format(distancia, str(distancia/0.45)))

def area(largura, comprimento):
    a = float(largura) * float(comprimento)
    print(f'A área de um terreno de {largura}x{comprimento} é {a}m²')


area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))

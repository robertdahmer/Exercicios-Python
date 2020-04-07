for c in range(0, 9):
    from pygame import mixer
    mixer.init()
    mixer.music.load('musica3.mp3.mp3')
    mixer.music.play()
    b = str(input('Quer continuar escutando?'))
    if b == 'não' or b == 'nao' or b == 'Não':
        print('Fodase continua ouvindo')
    from pygame import mixer

    mixer.init()
    mixer.music.load('musica3.mp3.mp3')
    mixer.music.play()
    

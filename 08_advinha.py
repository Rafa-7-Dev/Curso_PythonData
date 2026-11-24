#  _______ _____  ___ ___ _______ _______ _______ _______      _______ _______ _______ _______ 
# |   _   |     \|   |   |_     _|    |  |   |   |   _   |    |     __|   _   |   |   |    ___|
# |       |  --  |   |   |_|   |_|       |       |       |    |    |  |       |       |    ___|
# |___|___|_____/ \_____/|_______|__|____|___|___|___|___|    |_______|___|___|__|_|__|_______|
#
# Autor: Rafael Lima
# Versão 1.0.0
# Licença: OPEN SOURCE

from random import randint

random = randint(1, 100)
chute = 0
chances = 10

while chute != random : #Lemos da seguinte forma: enquanto "chute" for diferente do "random"...
    chute = input('chute um número de 0 a 100:')
    if chute.isnumeric() :
        chute = int(chute)
        chances = chances - 1
        if chute == random :
            print('')
            print('Parabéns, você advinhou! O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break
        else : 
            print('')
            if chute > random:
                print('Você errou! Dica: é um número menor')
            else :
                print('Você errou! Dica: é um número maior')
            print('Você ainda tem {} chances'.format(chances))
            print('')
        if chances== 0:
            print('')
            print('Suas chances acabaram, você perdeu e o número era {}'.format(random))
            print('')
            break
print('GAME OVER')

#Jogo da Adivinhação v1.0
from random import randint
from time import sleep
print('Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuárui venceu ou não a partida.')
##Lets go caraio!
print(' ----- I N I C I O ----- ')
jogador = int(input('Escolha um numero de 0 a 5: ').strip())
#Verificar se o burro não colocou outro valor além de 0 a 5: - http://excript.com/python/operadores-logicos-python.html
print('Processando . . .')
sleep(3)
if jogador <=5:
    computer = randint(0,5) #https://docs.python.org/pt-br/3/library/random.html
    if jogador == computer:
        print('YOU WIN!!!')
    else:
        print('YOU LOSEEEEER. Eu tinha escolhido o número {}.'.format(computer))
else:
    print('Oh meu querido, o numero é INVALIDO... ')
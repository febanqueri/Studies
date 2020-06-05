print('Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo')

import math
angulo1 = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo1))
print('O angulo de {} tem o SENO de {:.2f}.'.format(angulo1,seno))
cosseno = math.cos(math.radians(angulo1))
print('O angulo de {} tem o COSSENO de {:.2f}.'.format(angulo1,cosseno))
tangente = math.tan(math.radians(angulo1))
print('O angulo de {} tem a TANGENTE de {:.2f}.'.format(angulo1,tangente))

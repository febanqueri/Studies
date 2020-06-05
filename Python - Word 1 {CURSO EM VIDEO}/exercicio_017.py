'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.'''

'''co = float(input('Digite o valor do CATETO OPOSTO: '))
ca = float(input('Digite o valor do CATETO ADJACENTE: '))
hip = (co ** 2 + ca ** 2) ** (1//2)
print('A hipotenusa vai medir {:.2f}.'.format(hip))'''

#Segundo metodo:
import math
co = float(input('Digite o valor do CATETO OPOSTO: '))
ca = float(input('Digite o valor do CATETO ADJACENTE: '))
hi = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}.'.format(hi))
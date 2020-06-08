#PAr ou Impar
print('Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.')
num = int(input('Digite um numero: '))
resultado = num % 2
if resultado % 2:
    print('O numero digitado foi{}, ele é IMPAR {}.'.format(num,resultado))
else:
    print('O numero digitado foi {}, ele é PAR {}.'.format(num,resultado))

#Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
celsius = float(input('Qual a temperatura em Cº ?'))
fahr = (celsius* 9/5)+32
print('Transformando em Fº:{:.1f}.'.format(fahr))

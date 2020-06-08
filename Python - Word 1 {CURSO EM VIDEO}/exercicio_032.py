#Ano Bissexto
from datetime import date
print('Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.')
ano = int(input('Digite um ano para ser analisado. Digite 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #https://www.todamateria.com.br/ano-bissexto/
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!.'.format())

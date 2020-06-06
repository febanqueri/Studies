print('Crie um programa que leia o nome da uma cidade e diga se ela começa ou não com nome "SANTO"')
cidade = str(input('Qual o nome da sua cidade?')).strip() #Strip elimina espaços no começo e fim.
print(cidade[:5].upper() == 'SANTO')

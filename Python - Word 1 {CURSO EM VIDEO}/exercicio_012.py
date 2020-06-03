# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço
#com 5% de desconto.
product = float(input('Digite o valor do produto: '))
desconto=(product*5) /100
precofinal = product-desconto
print('Aplicado 5% de desconto, o valor será de {}'.format((precofinal)))


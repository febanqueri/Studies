# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Considerar US$1.00 = R$ 5,37
cash = float(input('Digite uma quantia em R$(Real brasileiro): '))
dolar = 5.37
print('Convertido para Dólar é {:.2f}.'.format(cash / dolar))

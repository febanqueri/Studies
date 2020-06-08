#Custo da Viagem
print('Desenvolva um programa que pergunta a distância de uma viagem em KM.\nCalcule o preço da passagem, cobrando R$ 0.50 por KM para viagens de até 200 KM e R$ 0.45 para viagens mais longas.')
km = float(input('Digite a distancia: '))
curta = 0.50
longa = 0.45
if km <= 200:
    print('O custo para a distância informada é R${:.2f}.'.format(curta * km))
else:
    print('O custo para a distancia informada é R${:.2f}.'.format(longa * km))

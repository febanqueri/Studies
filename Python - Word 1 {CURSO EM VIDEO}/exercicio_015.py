# Escreva um programa que pergunte a quantidade de KM percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que:
# Alguel por dia é R$ 60,00;
# KM rodado é R$ 0,15.
dias = int(input('Quantos dias o carro foi alugado?'))
percorrido = float(input('Quantos KM foi percorrido?'))
diafixo = 60
kmfixo = 0.15
diaria = diafixo * dias
kmtotal = kmfixo * percorrido
print('O valor  total de diaria foi de R$ {:.2f}.'.format(diaria))
print('O valor total de KM percorrido foi de R${:.2f}.'.format(kmtotal))
print('Com o TOTAL de R$ {:.2f}'.format(diaria+kmtotal))


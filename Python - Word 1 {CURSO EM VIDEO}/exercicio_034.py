#Aumentos multiplos.
print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.\n Para salário superiores a R$1200.00, calcule um aumento de 10%.\n Para inferiores ou igual, o aumento é de 15%.')
salario = float(input('Digite o valor do salário: '))
if salario <= 1250:
    novo = (salario * 15 / 100) + salario
else:
    novo = (salario * 10 / 100) + salario
print('O valor do novo salário é R${:.2f}.'.format(novo))

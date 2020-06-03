#Faça um algorotmo que leia o salario de um funcionário.
#Apresenta este salário com um aumento de 15%
salario = float(input('Digite o seu salário: '))
aumento = (salario*15)/100
print('O seu salário com o aumento de 15% fica em R$ {:.2f}.'.format(salario + aumento))
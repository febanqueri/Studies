#Primeiro e ultimo nome de uma pessa
print('Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente.')
nome = str(input('Digite o seu nome: ')).strip()
print('Sejá bem vindo!')
divide = nome.split()
print('Seu primeiro nome é {}.'.format(divide[0].capitalize()))
print('Seu ultimo nome é {}.'.format(divide[len(divide)-1].capitalize()))
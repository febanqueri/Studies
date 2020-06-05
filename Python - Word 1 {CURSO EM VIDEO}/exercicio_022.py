print('Crie um programa que leia o nome completo de uma pessoa e mostre: \n- O nome com todas as letras MAISCULAS e MINISCULAS; \n- Quantas letras ao todo(SEM CONSIDERAR OS ESPAÇOS); \n- Quantas letras tem o primeiro nome.')
print('------------------- I N I C I A N D O -------------------')
nome = str(input('Digite o seu nome completo:')).strip()
print('------------------- A N A L I S A N D O -------------------')
print('O seu nome com letras maiscula é: {}.'.format(nome.upper()))
print('O seu nome com letras minuscula é: {}.'.format(nome.lower()))
#Devemos desconsiderar os espaços para contar:
print('O seu nome possui ao todo {} letras.'.format(len(nome)-nome.count(' ')))
print('O seu PRIMEIRO nome possui {} letras.'.format(nome.find(' ')))

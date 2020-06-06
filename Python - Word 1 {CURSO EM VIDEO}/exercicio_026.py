#Primeira e ultima ocorrencia de uma string.
print('Faça um programa que leia uma frase pelo teclado e mostre: ')
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez;
#Em que posição ela aparece a ultima vez;

frase = str(input('Digite um frase qualquer: ')).strip().upper()
print('A letra A aparece {} vez na frase.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra A aparece para ultima vez na posiçaõ {}.'.format(frase.rfind('A')+1))
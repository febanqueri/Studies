print('O mesmo professor do exercicio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatros alunso e mostre a ordem sorteada.')
import random #Outra opção seria "from random import shuffle
#Ler os alunos:
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Teceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista) #Shuffle = Embaralhar
print('A ordem de apresentação será: ')
print(lista)
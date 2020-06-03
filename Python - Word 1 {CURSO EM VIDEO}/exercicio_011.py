#Faça um programa que leia a largura e a altura de uma parede.
#Calcule a sua area e a quantidade de tinta necessária para pinta-la.
#Sabe-se que cada 1 Litro de tinta, pinta uma area de 2m².
larg = float(input('Qual a largura da parede?(mts) '))
alt = float(input('Qual a altura da parede?(mts) '))
total = larg*alt
tinta = 2
necessario = total/tinta
print('A area da sua parede é de {}m².'.format((total)),end=' ')
print ('Será necessário {:.3f} Litros de tinta para pinta-la.'.format(necessario))
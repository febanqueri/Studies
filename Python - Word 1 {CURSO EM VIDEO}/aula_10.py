#Condições
#Exemplo
idade = int(input('Quanto anos voce tem?'))
if idade<=15:
    print('Ta novo ainda!')
else:
    print('Cuidado que a hora ta chegando...')
print('------ FIM ------\n\n\n\n\n\n')


#Segundo exemplo:
nota1 = float(input('Digite a NOTA 1: '))
nota2 = float(input('Digite a NOTA 2: '))
media = (nota1+nota2) / 2
print('Sua média é: {:.1f}.'.format(media))
if media >=7:
    print('Voce foi aprovado, parabens!')
else:
    print('Se fudeu, foi reprovado!')
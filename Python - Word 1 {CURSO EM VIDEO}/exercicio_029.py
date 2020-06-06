#Radar Eletronico
import emojis #https://pypi.org/project/emojis/ - https://www.webfx.com/tools/emoji-cheat-sheet/
print('Escreva um programa que leia a velocidade de um carro.\n Se ele ultrapassar 80 KMH. Mostre uma mensagem dizendo que ele foi multado.\n A multa vai custar R$7,00 por KM acima do permitido.')
velocidade = float(input('BIP BIP BIP - Qual a velocidade do carro {} ? '.format((emojis.encode(':car:')))))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/H.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma MULTA no valor de R${:.2f}.'.format(multa))
print('O Departamento de Trânsito agradece a atenção, tenha um bom dia.')


#Escreva um programa que leia um valor em metros e o exbia convertido em centimentros e milimetros.
medida = float(input('Digite uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {} correste a {:.0f}cm e {:.0f}mm.'.format(medida,cm,mm))

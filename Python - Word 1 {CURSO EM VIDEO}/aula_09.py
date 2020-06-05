#Manipulando Cadeias de Texto
exemplo = 'Uma frase qualquer, Doideira.'
#Explicação de alocação de memória.

print('Técnica de Fatiamento:')
#Técnica de Fatiamento
print(exemplo[2:5])
print(exemplo[2:10:2]) #Imprimi o que estiver dentro do espaço 2 até 9 de 2 em 2.
print(exemplo[:5]) #limita até onde será printado.
print(exemplo[5:]) #limita onde irá começar.
print(exemplo[9::3]) #limita o começo e indica o intervalo de 3 em 3

print('\n \n Técnica de Análise:')
#Técnica de Analise
print('Irá mostrar que o "COMPRIMENTO" do objeto é {}.'.format(len(exemplo)))
print('Irá "CONTAR" quantas vezes aparece o indice, no nosso caso é {}.'.format(exemplo.count('a')))
print('Irá "CONTAR" quantas vezes aparece o indice no espaco determinado, no nosso caso é {}.'.format(exemplo.count('a',0,12)))
print('Irá "ENCONTRAR" o inicio do o que sera determinado, no nosso caso {}.'.format(exemplo.find('fra')))
print('Se o que foi pedido no "ENCONTRAR" nao for localizado em deve trazer {}.'.format(exemplo.find('Dragao')))
print('Irá responder Sim/Não se existe X na string, no nosso caso é {}.'.format('frase'in exemplo))

#Técnica de Transformação
print('\n \n Técnica de Transformação:')
print('Irá "TROCAR" X por Y, nosso caso a frase ficou: {}'.format(exemplo.replace('Doideira','Oloquinho')))
#Replace = Substituir
print('Irá transformar o que não for MAISCULO, em MAISCULO. Nossa frase ficaria assim : {}'.format(exemplo.upper()))
print('Irá fazer o inverso, o que não for MINISCULO, ficara. Nossa frase ficaria assim: {}.'.format(exemplo.lower()))
print('Irá deixar apenas a PRIMEIRA LETRA MAISCULA.(da frase) Ficaria assim: {}'.format(exemplo.capitalize()))
print('Irá deixa a PRIMEIRA LETRA DE CADA PALAVRA MAIUSCULA, ficaria assim: {}'.format(exemplo.title()))
exemplo2= '   Frase com espaço.  '
print('Irá remover os espaços escedentes, fica assim: {}'.format(exemplo2.strip()))
#variações:
print('Irá remover os espaços, pela DIREITA. Exemplo: {}'.format(exemplo2.rstrip()))
print('Irá remover os espaços, pela ESQUERDA. Exemplo: {}'.format(exemplo2.lstrip()))


#Técnicas de Divisão:
print('\n \n Técnicas de Divisão:')
print('Gera uma divisão onde encontrar ESPAÇOS na frase. Assim dividindo em novas String, gerando uma lista para GUARDAR-LAS. Ficaria assim: {}'.format(exemplo.split()))


#Técnicas de Junção:
print('\n \n Técnicas de Junção:' )
print('Junta as string, separando-as com um "-". Ficaria assim: {}'.format('-'.join(exemplo)))

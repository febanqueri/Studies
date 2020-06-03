# Trabalhando com Módulos.
# Biblioteca "Random" - https://docs.python.org/pt-br/3/library/random.html
import random
num1 = random.random()
# O metodo ".random()" gera um numero aleatório entre 0 e 1 (type = float)
print(num1)
num2 = random.randint(1,10)
# O metodo ".randint()" gera um numero aleatorio inteiro, vc pode definir o invervalo.
print(num2)

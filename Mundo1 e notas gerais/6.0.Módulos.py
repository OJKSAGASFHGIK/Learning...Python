import math
a1 = int(input('Número: '))
b1 = math.sqrt(a1)
print(f'Raiz = {b1:.2f}')
print(f'Raiz com arredondamento pra cima = {math.ceil(b1)}')
print(f'Raiz com arredondamento pra baixo: = {math.floor(b1)}')
from math import sqrt
b2 = sqrt(a1)
print(f'Raiz usando "from math import sqrt" = {b2:.2f}')
print('A variável pode ser abreviada como sqrt(invés de "math.sqrt")')
print(input('===next==='))
import random
print('Estes são comandos "random." :')
print('Este número é random.random:',random.random())
print('de 0 a 1')
print('Este número é random.randint:',random.randint(3,27))
print('({3-27} - Ordem especificada)')
#Módulos interessantes:
# from time import sleep
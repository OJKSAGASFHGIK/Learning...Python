from math import sqrt, trunc,floor,ceil, hypot, radians,sin,cos,tan
from random import shuffle,choice
import pygame
#16
print('-Porção inteira:')
a1 = float(input('Número decimal: '))
print(f'Porção inteira = {trunc(a1)}')
input('===next===')
#17
print('Hipotenusa:')
a2 = float(input('Qual a largura do cateto adjacente? '))
a3 = float(input('E qual a altura do cateto oposto? '))
b1 = hypot(a2,a3)
print(f'A hipotenusa é igual a: {b1:.2f}')
input('===next===')
#18 - Estudar mais isso qualquer dia...
print('-Seno, cosseno e tangente:')
a4 = float(input('Digite o ângulo que você deseja: '))
b2 = sin(radians(a4))
b3 = cos(radians(a4))
b4 = tan(radians(a4))
print(f'Seno: {b2:.2f}\nCosseno: {b3:.2f}\nTangente: {b4:.2f}')
input('===next===')
#19
print('-Sorteio:')
a5 = str(input('Nome do primeiro aluno: '))
a6 = str(input('Nome do segundo aluno: '))
a7 = str(input('Nome do terceiro aluno: '))
a8 = str(input('Nome do quarto aluno: '))
b5 = [a5,a6,a7,a8]
print(f'{choice(b5)} foi escolhido(a).')
input('===next===')
#20
print('-Ordem:')
a9 = str(input('Primeiro aluno: '))
a10 = str(input('Segundo aluno: '))
a11 = str(input('Terceiro aluno: '))
a12 = str(input('Quarto aluno: '))
b6=[a9, a10, a11, a12]
shuffle(b6)
print('A ordem será:')
print(b6)
input('===next===')
#21
print('MÚSICA!!')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('watamote-op-full-version.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('LINHA DE COMANDO FINALIZADA!!')
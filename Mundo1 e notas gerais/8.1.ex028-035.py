from random import randint
#28:
a1 = randint(1,3)
a2 = int(input('Qual número eu estou pensando, entre 1 a 3? '))
if a1 == a2:
 print(f'Isso mesmo, eu estava pensando em {a1}.')
else:
 print(f'Droga, você errou. Eu estava pensando em {a1}.')
input('NEXT:===')
#29:
a3 = float(input('''Você vê uma placa indicando "limite de velocidade(80km)".
Em que velocidade você vai? '''))
b1 = float((a3-80)*7)
#80=limite de velocidade. 7=Multa a cada 1km
if 80 >= a3:
 print(f'Obrigado por andar dentro do limite e valorizar a existência.')
else:
 print(f'Você passou do limite, e vai pagar: R$ {b1}')
input('NEXT:===')
#30:
a4 = int(input('Escolha um número natural: '))
b2 = a4%2
if b2 == 0:
 print(f'O número {a4} é par.')
else:
 print(f'O número {a4} é impar.')
#31:
a5 = float(input('Quantos quilômetros vai ser sua viagem? '))
b3 = a5*0.50 if a5<=200 else a5*0.45
print(f'O preço da sua passagem será: R$ {b3:.2f}')
input('NEXT:===')
#32
from datetime import date
a6 = int(input('Que ano quer analizar? '))
if a6 == 0:
    a6 = date.today().year
if a6 % 4 == 0 and a6 % 100 != 0 or a6 % 400 == 0:
 print(f'O ano {a6}, é bissexto.')
else:
 print(f'O ano {a6}, não é bissexto.')
input('NEXT:===')
#33
a7 = int(input('Número 1: '))
a8 = int(input('Número 2: '))
a9 = int(input('Número 3: '))
# Menor:
b4 = a7
if a8<a7 and a8<a9:
    b4 = a8
if a9<a7 and a9<a8:
    b4 = a9
print(f'O menor número é {b4}')
# Maior:
b5 = a7
if a8>a7 and a8>a9:
    b5 = a8
if a9>a7 and a9>a8:
    b5 = a9
print(f'O maior número é {b5}')
input('NEXT:===')
#34:
a10 = float(input('Qual o salário do funcionário? '))
b6 = a10+(a10*0.10)
b7 = a10+(a10*0.15)
if a10>=1250:
 print(f'O aumento salárial para mais de 1250, será: {b6:.2f}' )
else:
 print(f'O aumento salárial para menos de 1250, será: R$ {b7:.2f}')
input('NEXT:===')
#35:
a11 = float(input('Qual a 1¹ base do triângulo? '))
a12 = float(input('Qual a 2¹ base do triângulo? '))
a13 = float(input('Qual a 3¹ base do triângulo? '))
if a11<a12+a13 and a12<a11+a13 and a13<a11+a12:
 print('É possível formar o triângulo.')
else:
 print('Impossível formar o triângulo.')
input('NEXT:===')
print('=-'*27)
print('LINHA DE COMANDO FINALIZADA!')
print('=-'*27)
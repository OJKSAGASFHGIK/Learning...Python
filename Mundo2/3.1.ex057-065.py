from random import randint
from time import sleep
#57
print(f'\33[97:41m E se você botar o gênero errado? \33[m')
a1 = str(input('Qual seu gênero [M/F],[O(Outro)]: ')).strip().upper()[0]
while a1 not in'MFO':
 a1 = str(input('''Por favor, informe um gênero de preferência.
[M/F/O]: ''')).strip().upper()[0]
 if 'M'in a1:
  print('Você é um homem.')
 elif 'F'in a1:
  print('Você é uma mulher.')
 else:
  print('Outro... certo!')
input('\33[31mNext:==>\33[m')
#58: (refinar)
a2 = randint(1,10)
sleep(0.5)
print('''Acabei de pensar em um número...
Será que você consegue adivinhar? ''')
sleep(1)
a5 = 0
a3 = False
while not a3:
 a5 += 1
 a4 = int(input('Qual seu palpite: '))
 if a4==a2:
  a3 = True
 else:
  if a4<a2:
   print('Um pouco mais... -> ')
  elif a4>a2:
   print('Um pouco menos... -> ')
print(f'Você acertou com {a5} tentativas. Legal! :)')
input('\33[31mNext:==>\33[m')
#59:
a6 = int(input('1¹ valor: '))
a7 = int(input('2¹ valor: '))
a8 = 0
while a8 != 5:
 a8 = int(input('''O que você deseja fazer com esses valores:
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa
= '''))
 if a8 == 1:
  print(f'{a6} + {a7} = {a6+a7}')
 elif a8 == 2:
  print(f'{a6} * {a7} = {a6*a7}')
 elif a8 == 3:
  if a6>a7:
   print(f'O maior é: {a6}')
  else:
   print(f'O maior é: {a7}')
 elif a8 == 4:
  a6 = int(input('1¹ valor: '))
  a7 = int(input('2¹ valor: '))
 else:
  print('Certo!')
 sleep(2)
print('Programa finalizado.')
input('\33[31mNext:==>\33[m')
#60.1
a9 = int(input('Escolha um número para fatorial: '))
b2 = 1
for b1 in range(a9,0,-1):
 b2 *= b1
print(f'O fatorial, é: {b2}')
input('\33[31mNext:==>\33[m')
#60.2
a11 = 1
a10 = int(input('Escolha um número para fatorial, novamente: '))
print(f'{a10}! = ',end='')
while a10 > 0:
 print(f'{a10}', end=' ')
 print('*' if a10 > 1 else '=', end=' ')
 a11 *= a10
 a10 -= 1
print(a11)
input('\33[31mNext:==>\33[m')
#61
print('\33[97:41m Progressão aritmética (PA): ex2 \33[m')
a12 = int(input('Primeiro termo: '))
a13 = int(input('Razão: '))
print('(', end= '')
a14 = 1
while a14<10+1:
 a14 += 1
 print(f'{a12}', end='')
 print(', ' if a14<11 else ')', end= '')
 a12 += a13
input('\33[31mNext:==>\33[m')
#62
print('\33[97:44m Progressão aritmética (PA): ex3 \33[m')
a15 = int(input('Número: '))
a16 = int(input('Razão: '))
a17 = 1
a18 = 10
a19 = 0
while a18 != 0:
 a19 += a18
 while a17<=a19:
  print(f'{a15}, ',end='')
  a17 += 1
  a15 += a16
 print('acabou.')
 a18 = int(input('Mais quantos termos quer: '))
print(f'\33[31mVocê mostrou {a19} resultados.\33[m')
input('\33[31mNext:==>\33[m')
#63
print('\33[97:41m Sequência de fibonacci \33[m')
a20 = int(input('Escolha um número: '))
a21 = 0
a22 = 1
b3 = a21+a22
print(a21, a22, b3, end=' ')
a23 = 4
while a20>=a23:
 a21 = a22
 a22 = b3
 b3 = a21+a22
 a23 += 1
 print(b3, end=' ')
input('\33[31mNext:==>\33[m')
#64
print('\33[97:41m Soma total e de números de valores \33[m')
a24 = int(input('Digite um valor, diferente de 999: '))
b4 = b5 = 0
while a24 != 999:
 b4 += a24
 b5 += 1
 a24 = int(input('Digite um valor, diferente de 999: '))
print(f'Total de números digitados: {b5} / Total: {b4}')
input('\33[31mNext:==>\33[m')
#65
print('\33[97:41m Calculadora de média, e comparador de valores \33[m')
a26 = 'S' #Condição de intermitência
b6 = b7 = 0 #Contador e média
b8 = b9 = 0 #Comparador
while 'S'in a26:
 b7 += 1
 a25 = int(input(f'{b7}¹ número: '))
 b6 += a25
 if b7 == 1:
  b8 = b9 = a25
 else:
  if a25>b8:
   b8=a25
  if a25<b9:
   b9=a25
 a26 = str(input('Quer continuar? \33[31m(S/N)\33[m: ')).upper()
print(f'Média = {b6/b7:.2f} / Comparação: {b8} > {b9}')
#Nesse caso, todos os números receberam os mesmos valores. E todos eles
# servem de comparação constante com o primeiro termo.
# Ex:
# b7 += 1
# if b7 == 1:
#  b8 = b9 = a25
input('\33[31mNext:==>\33[m')
print('\33[33m=+-\33[m'*9)
print('LINHA DE COMANDO FINALIZADA!!')
print('\33[31m=+-\33[m'*9)
#Tem questões que precisam ser corrigidas e refinadas.
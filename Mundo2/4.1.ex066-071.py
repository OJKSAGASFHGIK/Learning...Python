from random import randint
#66:
print('\33[97:41m Ex:66 / Quantidade e total de valores \33[m')
a2 = a3 = 0
while True:
 a1 = int(input('Digite um valor (\33[31m999 para parar\33[m): '))
 if a1 == 999:
  break
 a2 += 1
 a3 += a1
print(f'Você digitou {a2} valores. Totalizando: {a3}')
input('\33[31mNext:==>\33[m')
#67:
print('\33[97:41m Ex:67 / Tabuada \33[m')
while True:
 a4 = int(input('Digite um valor(\33[31mnegativo para parar\33[m): '))
 if a4<0:
  print('\33[33mTabuada finalizada\33[m')
  break
 for b1 in range(1,10+1):
  b2 = a4*b1
  print(f'{a4} * {b1} = {b2}')
input('\33[31mNext:==>\33[m')
#68: .upper().strip()[0]  (debug) , else: , break
print('\33[97:41m Ex:68 / Par ou ímpar \33[m')
a8 = 0
while True:
 a5 = randint(1, 10)
 a7 = int(input('Escolha um número: '))
 a6 = str(input('Par ou ímpar (\33[31mP/I\33[m) ? ')).upper().strip()[0]
 b3 = a5+a7
 if 'P'in a6:
  if b3%2 == 0:
   a8+=1
   print(f'''O computador escolheu {a5}.
Você acertou {a8} vez(es).''')
  else:
   print(f'''O computador escolheu {a5}.
Você perdeu com {a8} tentativa.''')
   break
 elif 'I'in a6:
  if b3%2 == 1:
   a8+=1
   print(f'''O computador escolheu {a5}.
Você acertou {a8} vez(es).''')
  else:
   print(f'''O computador escolheu {a5}.
Você perdeu com {a8} tentativa.''')
   break
input('\33[31mNext:==>\33[m')
#69: while V not in'str' (debug)
print('\33[97:41m Ex:69 / Listagem \33[m')
b4=b5=b6= 0
while True:
 print('\33[33mCadastro\33[m')
 a9 = int(input('Idade: '))
 if a9 >= 18:
  b4 += 1  #maiores de 18
#
 a10= ' ' #o acumulador de string, é separado.
 while a10 not in'MF': #você pode usar while como debug
  a10 = str(input('Sexo (\33[31mM/F\33[m): ')).upper().strip()[0]
  if 'M'in a10:
   b5 += 1 #t.homens
  elif 'F'in a10:
   if a9<=20:
    b6 += 1 #t.mulheres com menos de 20
#
 a11= ' '
 while a11 not in'SN':
  a11 = str(input('Quer continuar (\33[32mS/N\33[m)? ')).upper().strip()[0]
 if a11 == 'N':
  break
#
print(f'''Há {b4} pessoa(s) maior(es) de 18.
{b5} homem(ns), e {b6} mulher(es) com até 20 anos.''')
input('\33[31mNext:==>\33[m')
#70: V=0 , V+=1 , if V==1 or V2<T: , V2=T , V3=T2... (menor valor e atribuições)
print('\33[97:41m Ex:70 / Sistema de compra e venda \33[m')
b7=b8=b9=b11= 0
b10= ' '
while True:
 print('\33[33m-Novo produto \33[m')
 a12 = str(input('Nome do produto: '))
 a13 = float(input('Valor: '))
 b7 += a13 #t.valores
 a14 = ' '
#
 if a13>=1000:
  b8+=1 #valores no mínimo 1000
#
 b9+=1
 if b9 == 1 or a13<b9:
  b10 = a13 #menor valor
  b11 = a12 #nome do produto
#
 while a14 not in'SN':
  a14 = str(input('Quer continuar (S/N)? ')).upper().strip()[0]
 if a14 == 'N':
  break
print(f'O total da compra foi: {b7:.2f}.')
print(f'Com {b8} produto(s) no mínimo R$1000,00.')
print(f'O produto mais barato foi {b11}, e custou {b10:.2f}.')
input('\33[31mNext:==>\33[m')
#71:
# Extração numérica contínua / print e troca simultanea de variável
print('\33[97:41m Ex:71 / Saque de dinheiro \33[m')
a15 = int(input('Valor de saque: '))
b12 = a15
b13 = 50 #valor da cédula
b14 = 0
while True:
 if b12 >= b13: #
  b12 -= b13 #resto do dinheiro
  b14 += 1 #quantidade de cédulas
 else:
  if b14 > 0:
   print(f'{b14} cédulas de {b13}.')
  if b13 == 50:
   b13 = 20
  elif b13 == 20:
   b13 = 10
  elif b13 == 10:
   b13 = 1
  b14=0
  if b12 == 0:
   break
print('\33[31m+=-\33[m'*9)
print('LINHA DE COMANDO FINALIZADA!!')
print('\33[31m+=-\33[m'*9)
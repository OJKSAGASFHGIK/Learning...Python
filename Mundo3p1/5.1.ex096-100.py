from time import sleep
from random import randint
def beautifulTitleR(title):
 print(f'\33[97:41m {title} \33[m')
 print('\33[31m=\33[m'*(len(title)+2))
def beautifulTitleG(title):
 print(f'\33[97:42m {title} \33[m')
 print('\33[32m=\33[m'*(len(title)+2))
def next():
 input('\33[31mNext:===>\33[m')
def area(aa1,aa2):
 bb1=aa1*aa2
 print(f'A área do terreno {aa1}x{aa2}, é: \33[31m{bb1:.2f}\33[mm²')
def simpleCounter(aa3,aa4,aa5):
 cc1 = 1
 if aa4 > aa3:
  aa4 += 1
 elif aa4 < aa3:
  aa4 -= 1
  cc1 = 0
 while True:
  if cc1 == 0:
   if aa5 < 0:
    break
   else:
    aa5 = int(input('\33[33mDigite uma intercalação negativa: \33[m'))
  elif cc1 == 1:
   if aa5 > 0:
    break
   else:
    aa5 = int(input('\33[33mDigite uma intercalação positiva: \33[m'))
 print('\33[33mA ordem numérica, é: \33[31m')
 if aa5 != 0:
  for bb2 in range(aa3,aa4,aa5):
   print(bb2,end=' ')
   sleep(0.27)
 elif aa5 == 0:
  for bb2 in range(aa3,aa4+1,1):
   print(bb2,end=' ')
   sleep(0.27)
 print('\33[m')
def maxMin(*aa6):
 aa7=aa8= 0
 for bb3,bb4 in enumerate(aa6):
  if bb3 == 0:
   aa7=aa8= bb4
  else:
   if aa7<bb4:
    aa7= bb4 #Maior
   if aa8>bb4:
    aa8= bb4 #Menor
  print(f'{bb4}', end=' ')
  sleep(0.27)
 print(f'são \33[31m{len(aa6)}\33[m valores ao todo.')
 print(f'O maior valor, é: \33[31m{aa7}\33[m.')
 print(f'O menor valor, é: \33[31m{aa8}\33[m.')
 print('\33[31m+=-\33[m'*9)
def randint1to10inPairs(aa9):
 print(f'Sorteando os \33[33m{aa9} valores\33[m da lista:',end=' ')
 aa11 = list()
 for bb5 in range(aa9):
  aa10 = randint(1,10)
  sleep(0.27)
  print(aa10,end=' ')
  aa11.append(aa10)
 aa12 = 0
 for bb6 in aa11:
  if bb6 % 2 == 0:
   aa12 += bb6
 print(f'\nA soma dos pares, é: \33[31m{aa12}\33[m')
def randint1to10(aa13):
 print('Números sorteados:',end=' ')
 for bb7 in range(5):
  sleep(0.27)
  aa14 = randint(1,10)
  print(f'\33[33m{aa14}\33[m',end=' ')
  aa13.append(aa14)
def sumPairs(aa13):
 aa15 = 0
 for bb8 in aa13:
  if bb8 % 2 == 0:
   aa15 += bb8
 print(f'\nA soma de todos os valores pares, é: \33[31m{aa15}\33[m')
#sleep(): maxMin(,) , randint1to10inPairs() , randint1to10()
#randint(): randint1to10inPairs() , randint1to10()
#96:
beautifulTitleR('Ex:96 / Área de um quadrado/retângulo')
a1 = float(input('Comprimento (m): '))
a2 = float(input('Largura (m): '))
area(a1,a2)
next()
#97:
beautifulTitleG('Ex:97 / Texto bonito...')
next()
#98: (atenuar se necessário {faltou a pratica do flush nessa resolução, e o uso do while})
beautifulTitleR('Ex:98 / Contador com debbug: ')
a3 = int(input('Primeiro número: '))
a4 = int(input('Número final: '))
a5 = int(input('Intercalação: '))
simpleCounter(a3,a4,a5)
next()
#99: (atenuar se necessário {faltou a pratica do flush nessa resolução})
beautifulTitleG('Ex:99 / Comparadores')
maxMin(3,2,1)
maxMin(-3,21,2,4,6)
maxMin(3,5,2)
maxMin()
next()
#100.1:
beautifulTitleG('Ex:100.1 / Gerador de números com soma em pares')
randint1to10inPairs(9)
next()
#100.2
beautifulTitleG('Ex:100.2 / Gerador de números com soma em pares')
aa16 = list()
randint1to10(aa16)
sumPairs(aa16)
next()
#
print('\33[32m+=-'*9)
print('\33[31mLINHA DE COMANDO FINALIZADA!!')
print('\33[33m-=+'*9)
# a5 aa16 bb8 cc1
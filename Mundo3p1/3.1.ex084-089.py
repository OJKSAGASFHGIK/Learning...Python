from time import sleep
from random import randint
#84: .index(min())
print('\33[97:41m Ex:84.1 / Comparador com .index(min()) \33[m')
a1 = ''
a2 = ['',0]
a3 = list()
while a1 != 'N':
 a2[0] = (str(input('Nome: ')))
 a2[1] = (float(input('Peso: ')))
 a3.append(a2[:])
 a1 = str(input('(S/N): ')).upper()
a4 = list()
a6 = list()
for b1 in a3:
 a4.append(b1[1])
 a6.append(b1[1])
a5 = a4.index(max(a4))
a7 = a6.index(min(a6))
#a6 = a4.index(min(a4)) corrigir
print(f'\33[33mVocê cadastrou {len(a3)} pessoas.\33[m')
print(f'O mais pesado é: {a3[a5][0]} com {a3[a5][1]}Kg.')
print(f'O mais leve é: {a3[a7][0]} com {a3[a7][1]}Kg.')
sleep(2.43)
print('\33[32mEssa solução não funciona se 2 pessoas tiverem o mesmo peso.\33[m')
input(f'''\33[31m{'next:':.^21}\33[m''')
#84.2:
print('\33[97:41m Ex:84.2 / Comparador bruto com números iguais \33[m')
a8= ['',0]
a12= []
a9=a10= 0
a11 = ''
while a11 != 'N':
 a8[0] = str(input('Nome: '))
 a8[1] = int(input('Peso: '))
 if len(a12) == 0:
  a9 = a8[1]
  a10 = a8[1]
 else:
  if a9 > a8[1]:
   a9 = a8[1]
  elif a10 < a8[1]:
   a10 = a8[1]
 a12.append(a8[:])
 a11 = str(input('Quer continuar? (S/N): ')).upper()
print(f'\33[31mTotal de cadastros: \33[33m{len(a12)}\33[m')
sleep(2.43)
print('\33[31mMaiores:\33[m')
for b2 in a12:
 if a9 == b2[1]:
  print(f'{b2[0]}',end=', ')
print(f'com {a9}Kg.')
print('\33[31mMenores:\33[m')
for b2 in a12:
 if a10 == b2[1]:
  print(f'{b2[0]}',end=', ')
print(f'com {a10}Kg.')
input(f'''\33[31m{'next:':.^21}\33[m''')
#85
print('\33[97:41m Ex:085 / Ímpares e pares (7 cadastros) \33[m')
a14= [[],[]]
for b3 in range(1,8):
 a13 = int(input(f'Digite o ¹{b3} valor: '))
 if a13 % 2 == 0:
  a14[0].append(a13)
 elif a13 % 2 == 1:
  a14[1].append(a13)
print('\33[31m+=-\33[m'*9)
print(f'Pares: {sorted(a14[0])}')
print(f'Ímpares: {sorted(a14[1])}')
input(f'''\33[31m{'next:':.^21}\33[m''')
#86.1:
print(f'\33[97:41m Ex:86.1 / Matriz com resultado horizontal e vertical \33[m')
a15 = [[],[],[]]
a16 = [[],[],[]]
for b4 in range(0,3):
 a15[0].append(int(input(f'Valor para (0,{b4}): ')))
 a16[b4].append(a15[0][b4])
for b4 in range(0,3):
 a15[1].append(int(input(f'Valor para (1,{b4}): ')))
 a16[b4].append(a15[1][b4])
for b4 in range(0,3):
 a15[2].append(int(input(f'Valor para (2,{b4}): ')))
 a16[b4].append(a15[2][b4])
print(f'''{a15[0]}
{a15[1]}
{a15[2]}''')
print('===')
print(f'''{a16[0]}
{a16[1]}
{a16[2]}''')
input(f'''\33[31m{'next:':.^21}\33[m''')
#86.2:
print(f'\33[97:41m Ex:86.2 / Matriz simplificada 3 por 3 \33[m')
a17 = [[],[],[]]
for b5 in range(0,3):
 for b6 in range(0,3):
  a17[b5].append(int(input(f'Digite um valor para, ({b5},{b6}): ')))
for b5 in range(0,3):
 for b6 in range(0,3):
  print(f'[{a17[b5][b6]:^4}]',end='')
 print()
sleep(3.24)
print('\33[33m+=-'*3,'\33[m')
sleep(0.81)
#87:
print('\33[97:43m Ex:87 / Bananada esse, vou nem descrever \33[m')
a18 = 0
for b7 in range(0,len(a17)):
 a18 += sum(a17[b7])
print(f'''Soma de todos os valores pares: {a18}
Soma dos valores da terceira coluna: {sum(a17[2])}
Maior valor da segunda linha: {max(a17[1])}''')
input(f'''\33[31m{'next:':.^21}\33[m''')
#88:
print('\33[97:41m Ex:88 / Sorteio com resultados em 1 variável \33[m')
a19 = []
a20 = list()
a21 = int(input('Digite a quantidade de sorteios: '))
for b8 in range(0,a21):
 while len(a19) < 6:
  a19.append(randint(1,60))
 a20.append(a19[:])
 a19.clear()
 a20[b8].sort()
 print(f'Jogo {b8+1} = {a20[b8]}')
 sleep(0.81)
input(f'\33[31m{"next:":.^21}\33[m')
#89:
print('\33[97:41m Ex:89 / Médias com verificador de notas \33[m')
a22 = [[''],[0]]
a23 = 'S'
a24 = list()
a25 = [0,0]
while a23 == 'S':
 a22[0] = str(input('Nome: '))
 for b9 in range(0,2):
  a25[b9] = float(input('Nota: '))
 a22[1] = sum(a25)/2 #média
 a22.append(a25[:]) #pontos
 a23 = str(input('Continuar? (S/N): ')).upper()
 a24.append(a22[:]) #todos os resultados
 del(a22[2])

for b10 in range(0,len(a24)):
 print(f'\33[31m[{b10}]\33[m = {a24[b10][0]} - Média: {a24[b10][1]:.2f}')
a26 = -2
print('\33[31m-1\33[33m para parar de ver as notas.\33[m')
while a26 != -1:
 a26 = int(input('Qual das notas você quer ver: '))
 if a26>-1 and a26<len(a24):
  print(f'{a24[a26][0]} - Notas: {a24[a26][2]}')
print('\33[32m+=-'*9)
sleep(0.81)
print('\33[31mLINHA DE COMANDO FINALIZADA!!')
sleep(0.81)
print('\33[33m+=-'*9)
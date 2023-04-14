#https://www.youtube.com/watch?v=YV_JQmZNFsk
#5:58 - V2.append(V1[:]) - (lista dentro lista) , 8:03 - V2 = [V1[],V1[],V1[]]
#- (índices) , 9:20 - V2 = [V[0][0]] - (Extração especifica) , 11:27
#- V2= [[V1]] - (Extração simples)
#Prática:
# V.clear()
from time import sleep
a1 = list()
a2 = list()
for b1 in range(0,3):
 a1.append(str(input(f'Nome: ')))
 a1.append(int(input(f'Idade: ')))
 a2.append(a1[:])
 a1.clear()
 print('\33[31m===\33[m')
sleep(0.81)
for b2 in a2:
 print(b2[0])
sleep(0.81)
a3 = str(input('Você quer ver a idade de algum deles? (S/N): ')).upper()
if 'S'in a3:
 a4 = int(input('Qual deles? (0,2): '))
 print(f'{a2[a4][0]} tem {a2[a4][1]} anos.')
 input('\33[31mCerto, vamos prosseguir (enter):\33[m')
else:
 input('\33[31mCerto, vamos prosseguir (enter):\33[m')
#
print('\33[97:41m Vamos ver se alguma dessas pessoas são +18: \33[m')
sleep(2.43)
a5 = list()
a6 = 0
for b3 in a2:
 if b3[1] >= 18:
  a5.append(b3[0])
  a6 += 1
if a6 > 0:
 print(f'''\33[31mT.pessoas +18 = {a6}\33[m
{a5}''')
elif a6 == 0:
 print('\33[31mNinguém é maior de idade.\33[m')
sleep(2.43)
print('\33[32m+=-'*9)
sleep(0.81)
print('\33[31mLINHA DE COMANDO FINALIZADA!!')
sleep(0.81)
print('\33[33m-=+'*9)

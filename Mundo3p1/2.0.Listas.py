#https://www.youtube.com/watch?v=N1hTsbW50eM
#Teórica:
# 4:10, 5:54 - .append(''), 6:36 - .insert(0,''), 7:39 - del v[0] ,
# .pop(0) , .pop() , .remove('') , if 'str'in v: v.remove('str') ,
# v=list(range(3,9)) , v=[0,3,9,27] , v2.sort(v) , v2.sort(reverse=True) ,
# v=[0,3,9] len(v) (valores)
#Prática:
from time import sleep
a1 = [3, 9, 3, 3]
print(a1)
a2 = int(input('Digite um valor para alterar 9: '))
a1[1] = a2
print(a1)
print('\33[34m===\33[m')
a3 = int(input('Acrescente um valor (obs: os números serão deslocados): '))
a1.append(a3)
a1.sort(reverse=True)
print(a1)
sleep(3.6)
print(f'Essa lista tem: {len(a1)} elementos.')
print('\33[34m===\33[m')
a4 = int(input('Insira um valor na posição 2: '))
a1.insert(2, a4)
print(a1)
a1.pop()
sleep(2.7)
print('''Isso é repentino, mas do nada, o último valor foi excluido por
\33[31m.pop()\33[m''')
sleep(3.6)
print(a1)
a5 = int(input('Vamos esquecer isso. Digite outro valor: '))
if a5<len(a1):
 a1.pop(a5)
 print('\33[31mVOCÊ APAGOU OUTRO VALOR!!\33[m')
else:
 print('Ufa, você digitou um valor muito alto. Está tudo ok.')
sleep(2.4)
print(a1)
a6 = int(input('Acrescente um valor: '))
a1.append(a6)
for b1,b2 in enumerate(a1):
 print(f'Na posição {b1}: {b2}')
 sleep(0.5)
print('\33[34m===\33[m')
sleep(3.6)
print('Agora vamos adicionar vários valores a essa lista.')
for b3 in range(0,4):
 a1.append(int(input(f'Digite o ¹{b3+1} valor: ')))
sleep(0.9)
print(a1)
sleep(1.8)
a7 = a1[:]
a7[1] = int(input('Digite um valor: '))
print('Vamos criar uma cópia, e alterar o 2¹ valor.')
sleep(1.5)
print(f'Primeira lista: {a1}')
print(f'Cópia: {a7}')
sleep(4.5)
print('''E essa foi a parte bruta, de alguns comandos bases de lista.
\33[31mBoa sorte...\33[m''')
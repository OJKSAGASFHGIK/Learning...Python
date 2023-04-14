#Teórica:
# 9:03 - break. 10:54 - break. 11:06 - while True.
# 11:30 - o que faz um break.
#Prática:
# 18:59 -
#Minuto atual: 20:20
#t1: Continuidade simples
print('\33[97:41m t1: Continuidade simples \33[m')
a1 = 0
while True:
 a1 += 1
 print(a1, end=' ')
 if a1 == 10:
  break
input('\n\33[31mNext:==>\33[m')
#t2: Quebrando input pela raiz
print('\33[97:41m t2: Quebrando input pela raiz \33[m')
a3 = 0
while True:
 a2 = int(input('Digite um valor diferente de 0: '))
 if a2 == 0:
  break
 a3 += a2
print(f'Total: {a3}')
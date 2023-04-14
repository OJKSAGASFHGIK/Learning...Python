from time import sleep
#78: V.index(max(V)) , (atenuar se necessário)
print('\33[97:45m Ex:78 / Comparador com posição \33[m')
a1 = []
a2=a3= 0
for b1 in range(1,6):
 a1.append(int(input(f'Digite o {b1}¹ valor: ')))
a2 += a1.index(max(a1))
a3 += a1.index(min(a1))
print(a1)
print(f'O maior é \33[35m{max(a1)}\33[m',end=' ')
print(f'na posição \33[35m{a2}\33[m')
print(f'O menor é \33[35m{min(a1)}\33[m',end=' ')
print(f'na posição \33[35m{a3}\33[m')
input(f'\33[31mNext:==>\33[m')
#79: (atenuar se necessário)
print('\33[97:41m Ex:79 / A lista vai ficar em ordem crescente, sem números repetidos \33[m')
a4 = list()
while True:
 a5 = int(input('Digite um valor: '))
 if a5 not in a4:
  a4.append(a5)
 else:
  print('Apenas valores diferentes.')
 a6 = str(input('Quer continuar? (S/N): ')).upper()
 if a6 not in 'S':
  break
print(f'A lista é: {sorted(a4)}')
input(f'\33[31mNext:==>\33[m')
#80: (atenuar se necessário)
print('\33[97:41m Ex:80 / Os números serão comparados em simultâneo \33[m')
a7 = []
a9 = 0
for b1 in range(0,5):
 a8 = int(input('Digite um valor: '))
 if b1 == 0 or a8 > a7[-1]:
  a7.append(a8)
 else:
  while a9 < len(a7):
   if a8 <= a7[a9]:
    a7.insert(a9,a8)
    break
   a9 += 1
print(a7)
input('\33[31mNext:==>\33[m')
#81:
print('\33[97:41m Ex:81 / Quantos valores 5? Qual o total? Em ordem decrescente!? \33[m')
a10= list()
while True:
 a10.append(int(input('Digite um valor: ')))
 a11 = str(input('Continuar? (S/N): ')).upper()
 if 'N'in a11:
  break
if 5 in a10:
 a11 = a10.count(5)
 print(f'Há {a11} valor(es) 5.')
else:
 ''
a10.sort(reverse=True)
print(f't.valores: {len(a10)}')
print(a10)
input('\33[31mNext:==>\33[m')
#82
print('\33[97:41m Ex:82 / Pares e ímpares \33[m')
a14= list()
a15= list()
a16= list()
while True:
 a12 = int(input('Digite um valor: '))
 a16.append(a12)
 a13 = str(input('continuar? (S/N): ')).upper()
 if a12%2==0:
  a14.append(a12)
 elif a12%2==1:
  a15.append(a12)
 if 'N'in a13:
  break
print(f'''T.valores: {a16}
Valores pares: {a14}
Valores ímpares: {a15}''')
input('\33[31mNext:==>\33[m')
#83: (atenuar se necessário)
print('\33[97:41m Ex:83 / Buscando validez entre parênteses \33[m')
a17= str(input('Questão com parênteses: '))
a18= list()
for b2 in a17:
 if '(' == b2:
  a18.append('(')
 elif ')' == b2:
  if len(a18) > 0:
   a18.pop()
  else:
   a18.append(')')
   break
if len(a18) == 0:
 print('Essa expressão é válida.')
else:
 print('Essa expressão é inválida.')
input('\33[31mNext:==>\33[m')
sleep(2.43)
print('\33[32m+=-'*9)
sleep(0.81)
print('\33[31mLINHA DE COMANDO FINALIZADA!!')
sleep(0.81)
print('\33[33m-=+'*9,'\33[m')

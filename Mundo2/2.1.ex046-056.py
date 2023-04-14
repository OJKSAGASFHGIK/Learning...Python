from time import sleep
from datetime import date
#46
for a1 in range(10, 0, -1):
 print(a1)
 sleep(1)
print('\33[7:97:41m BOOOOOMMMMMM!!! \33[m')
input('NEXT:===')
#47
a2 = int(input('Número para conversão em pares: '))
for b1 in range(0, a2+1, 2):
 print(b1, end=' ')
input('\nNEXT:===')
#48
a3 = 0
a4 = 0
for b2 in range(0,501,3):
 if b2 % 2 == 1:
  a3 += 1
  a4 += b2
print(f'A soma dos {a3} valores ímpares, é: {a4}')
input('NEXT:===')
#49
a5 = int(input('Escolha um número para tabuada: '))
for b3 in range(1, 10 + 1):
 print(f'{a5} * {b3} = {a5*b3}')
input('NEXT:===')
#50: v=0 , if v1%2==0 , v+=1 , print(v)
a7 = 0
a8 = 0
for b4 in range (1,6+1):
 a6 = int(input(f'{b4}¹ Número: '))
 if a6%2 == 0:
  a7 += 1
  a8 += a6
print(f'A soma do(s) {a7} número(s) par(es), é:',a8)
input('NEXT:===')
#51: (atenuar se necessário)
a9 = int(input('Primeiro termo: '))
a10 = int(input('Razão: '))
b6 = a9 + (10-1) * a10 #fórmula matemática
for b5 in range (a9, b6+a10, a10):
 print(b5,end='\33[36m → \33[m')
print('end')
input('NEXT:===')
#52.1
a11 = int(input('Teste de número primo: '))
if a11 == 2 or a11 == 3 or a11 == 5 or a11 == 7:
 print(f'{a11} é primo.')
elif a11 % 2 == 0 or a11 % 3 == 0 or a11 % 5 == 0 or a11 % 7 == 0:
 print(f'{a11} não é primo.')
input('NEXT:===')
#52.2: v=0 , if: , v+=1 (atenuar se necessário)
a12 = int(input('Teste de número primo 2: '))
a13 = 0
for b7 in range(1, a12+1):
 if a12%b7 == 0:
  a13 += 1
print(f'O número {a12}, possui {a13} divisores.')
if a13 == 2:
 print('E é um número primo.')
else:
 print('E não é primo.')
input('NEXT:===')
#53: V2 = '' , for W in range() , V2 += V[W]
a14 = str(input('Escreva algo, e teste se é palíndromo: ')).strip().lower()
a14 = a14.split()
a14 = ''.join(a14)
a15 = ''
for b8 in range(len(a14)-1,-1,-1):
 a15 += a14[b8]
print(f'O inverso de {a14} é {a15}.')
if a14 == a15:
 print('É palíndromo. ')
else:
 print('Não é palíndromo.')
input('NEXT:===')
#54:
print(' \33[41m "Comparador" de idade \33[m ')
a16 = 0
a17 = 0
for b9 in range(1,7+1):
 a18 = int(input(f'Ano de nascimento do ¹{b9} candidato: '))
 a19 = date.today().year - a18
 if a19 >= 18:
  a16 += 1
 else:
  a17 += 1
print(f'''São maiores de idade: {a16} 
São menores de idade: {a17}''')
input('NEXT:===')
#055.1
#Nesse caso, vemos que uma 'V de for dentro de if == 1', serviu para
# fazer um comparador em 'if dentro de else'.
print('\33[41m "Comparador" de peso \33[m')
a21 = 0
a22 = 0
for b10 in range(1,5+1):
 a20 = float(input(f'{b10}¹ peso: '))
 if b10 == 1: #valores contidos
  a21 = a20
  a22 = a20 #valores distribuidos
 else:
  if a20>a21:
   a21=a20
  if a20<a22: #valores sendo comparados
   a22=a20
print(f'''Maior peso: {a21}
Menor peso: {a22}''')
input('NEXT:===')
#055.2
print('\33[41m Mais um tipo de "comparador" \33[m')
a23 = []
for b11 in range(1,4+1):
 a24 = float(input(f'{b11}¹ número: '))
 a23 += [a24]
print(f'''Maior número: {max(a23)}
Menor número: {min(a23)}''')
input('NEXT:===')
#056
b13 = 0
b15 = ''
b16 = 0
b17 = 0
for b12 in range(1,4+1):
 print(f'\33[{30+b12}m{b12}¹ Candidato: \33[m')
 a25 = str(input('Nome: '))
 a26 = int(input('Idade: '))
 a27 = str(input('''[\33[31mM\33[m/\33[31mF\33[m] - masculino ou feminino
Gênero: ''')).strip()
#
 b13 += a26
 b14 = b13/b12 #Média de idade do grupo
#
 if a27 in 'Mm' and b12 == 1:
  b15 = a25 #nome
  b16 = a26 #idade
 if a27 in 'Mm' and b16 < a26:
  b15 = a25 #nome e idade filtrados:
  b16 = a26 # do homem mais velho.
#
 if a27 in 'Ff' and a26<20:
  b17 += 1 #Número de mulheres com menos de 20:
#
print(f'''A média de idade do grupo, é: {b14:.2f}
O nome do homem mais velho, é {b15} e ele possui {b16} anos.
Também a {b17} mulher(es) com menos de 20 anos.''')
input('NEXT:===')
print('\33[31m+=-\33[m'*9)
print('LINHA DE COMANDO FINALIZADA!')
print('\33[33m+=-\33[m'*9)
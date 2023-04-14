#Comandos de aleatoriedade: random.sample()
from random import sample
#72:(V[input])
print('\33[97:41m Ex:72 / Número por extenso \33[m')
a1 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
      'nove','dez','onze','doze','treze','quatorze','quinze','dezesseis',
      'dezessete','dezoito','dezenove','vinte')
a2 = int(input('Digite um número entre \33[31m0 a 20\33[m: '))
while a2>20:
 a2 = int(input('Ocorreu um problema... tente de novo \33[31m(0 a 20)\33[m: '))
print(f'Você digitou \33[31m{a1[a2]}\33[m.')
input(f'''\33[31m{'>':>>9}\33[m''')
#73: .sorted()
print('\33[97:41m Ex:73 / Campeonato de xadrez \33[m')
a3 = ('Supi','Fier','Mekhitarian','Barbosa','Lima','Santiago',
 'Di Berardino','Quintiliano','Matsuura','Molina','Proudian',
 'Bittencourt','Umetsubo','Santos','Limp','Rodrigues','Cadilhac',
 'Oliveira','Filgueiras','Labussiere')
print('\33[31mPrimeiros colocados:\33[m')
for b1 in range(0,4+1):
 print(f'¹{b1+1}: {a3[b1]}')
input('\33[33m>>>\33[m')
print('\33[31mÚltimos colocados:\33[m')
for b2 in range(16,19+1):
 print(f'¹{b2+1}: {a3[b2]}')
input('\33[33m>>>\33[m')
print('\33[31mNomes:\33[m', sorted(a3))
print('\33[33m',a3[8-1],' está na 8¹ posição.\33[m')
input(f'''\33[31m{'>':>>9}\33[m''')
#74: .sample()
print('\33[97:41m Ex:74 \33[m')
a4 = tuple(sample(range(1,10),5))
print('\33[31mValores aleatórios:\33[m',a4,
      '\n\33[31mMaior:\33[m',max(a4),
      '\n\33[31mMenor:\33[m',min(a4))
input(f'''\33[31m{'>':>>9}\33[m''')
#75:
print('\33[97:41m Ex:75 / Resultados múltiplos \33[m')
a5 = int(input(f'1¹ valor: '))
a6 = int(input(f'2¹ valor: '))
a7 = int(input(f'3¹ valor: '))
a8 = int(input(f'4¹ valor: '))
b3 = (a5, a6, a7, a8)
print(f'O valor 9 apareceu {b3.count(9)} vez(es).') #
if 3 in b3:
 print(f'O número 3 foi encontrado na posição {b3.index(3) + 1}.') #
else:
 print('o número 3 não foi encontrado.')
print('Os valores pares, foram:', end= ' ')
for b4 in b3:
 if b4%2==0:
  print(b4, end=' ')
input(f'''\33[31m{'>':>>9}\33[m''')
#76:
print('\33[97:40m Ex:76 / Lista de compras: \33[m')
a9 = ('Ovos (30 únidades)', 15.00, 'Arroz (5kg)', 16.99,
      'Feijão (2kg)', 15.19, 'Sardinha (1kg)', 13.59,
      'Laranja Pera', 1.99, 'Limão Tahiti', 2.49,
      'Pães (6 únidades)', 2.00, 'Cream Cracker (400g)', 3.10)
for b5 in range(0,len(a9)):
 if b5%2==0:
  print(f'{a9[b5]:.<27}',end= '')
 else:
  print(f'R$ {a9[b5]:>6.2f}')
input(f'''\33[31m{'>':>>9}\33[m''')
#77:
print('\33[97:41m Ex:77 \33[m')
a10 = ('Pedra','Pena','Construir','Destruir','Sentimento',
       'Vitalidade')
for b6 in a10:
 print(f'\n{b6}:', end=' ')
 for b7 in b6:
  if b7.lower() in'aeiou':
   print(b7, end=' ')
print('\n\33[31m Essas são as vogais dessas palavras. \33[m')
input(f'''\33[31m{'>':>>9}\33[m''')
print('\33[31m-=+'*18)
print('\33[32m LINHA DE COMANDO FINALIZADA!!')
print('\33[33m+=-'*18)
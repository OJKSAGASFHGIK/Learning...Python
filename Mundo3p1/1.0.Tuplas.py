#https://www.youtube.com/watch?v=0LB3FSfjvao
#Teórioca:
# 10:10 - Simples e compostas. 10:40 - Possibilidades compostas.
# 11:43 - Elementos. 12:25 - String é variável composta. 13:03 - Fatiamento.
# 14:07 - Último elemento. 14:38 - Tipos de fatiamento. 15:38 - Tuplas em len.
# 16:00 - Tuplas em for. 18:39 - Tuplas são imutáveis.
#Comandos novos:
# .enumerate() , .sorted()
#Prática:
#t1: V = ('','','')
a1 = ('maçã', 'banana', 'laranja.')
print(f'''A primeira lista tem algumas frutas, como:
{a1}''')
input(f'''\33[33m{'next:':=>9}\33[m''')
#t2: V = '','',''
a2 = 'cenoura', 'cebola', 'abobrinha'
print(f'''A segunda lista tem alguns legumes, como:
{a2}''')
input(f'''\33[33m{'next:':=>9}\33[m''')
#t3: tupla , V[0]
a3 = int(input('Qual item da segunda lista (0,2): '))
print(a2[a3])
input(f'''\33[33m{'next:':=>9}\33[m''')
#t4:
print(a1[-1])
input(f'''\33[33m{'next:':=>9}\33[m''')
#t5: último elemento ignorado
print(a1[0:2])
input(f'''\33[33m{'next:':=>9}\33[m''')
#t6:
print(a2[1:])
input(f'''\33[33m{'next:':=>9}\33[m''')
#t7: ele sempre vai ignorar, nn esquece
print(a1[:2])
#t8:
print('\33[31mResposta simples: \33[m')
for b1 in a1:
 print(f'Comi {b1}.')
input(f'''\33[33m{'next:':=>9}\33[m''')
print('\33[31mResposta pra situações complexas: \33[m')
for b2 in range(0,len(a1)):
 print(f'Comi {a1[b2]} na posição {b2}.')
input(f'''\33[33m{'next:':=>9}\33[m''')
for b3,b4 in enumerate(a1):
 print(f'Comi {b4} na posição {b3}.')
input(f'''\33[33m{'next:':=>9}\33[m''')
print('Chega de comer. Comi pra caramba...')
input(f'''\33[33m{'next:':=>9}\33[m''')
#t9: .sorted() (ordem alfabética)
print(f'{sorted(a1)}')
input(f'''\33[33m{'next:':=>9}\33[m''')
#t10:
a4 = (27, 81, 243, 0)
a5 = (0, 1, 3, 9)
b5 = a5+a4
print(b5)
print(f'A tupla mista, possui {len(b5)} elementos.')
print(f'A tupla mista, possui {b5.count(9)} elemento 9.')
print(f'O elemento 9 está na casa {b5.index(9)} (\33[31mprimeiro elemento = 0\33[m). ')
print(f'O segundo elemento 0, está na casa {b5.index(0,1)}') #deslocamento
input(f'''\33[33m{'next:':=>9}\33[m''')
#t11:
a6 = ('Chimbinha', 10, 'M', 67.84)
print(a6)
del(a6)
print('Apagamos Chimbinha por questões de segurança.')

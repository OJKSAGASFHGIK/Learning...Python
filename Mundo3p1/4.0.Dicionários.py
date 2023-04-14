#https://www.youtube.com/watch?v=ZWj8o692qGY
#Teórica:
# v = dict() - 4:55, v = {'dict':'str','dict(num)':int} - 5:25,
# v['dict']=x - 6:45(append é simplificado em dicionários), del v['dict'] - 7:25,
# "(estruturando dicionários)" - 7:51, .values() .keys() .items() - 9:05,
# for b1,b2 in v1.items(): - 10:30, "(dicionários dentro de listas)" - 11:38
#Prática e exercícios:
# v2list.append(v1dict.copy())
# from operator import itemgetter
# sorted(dict.items(),key=itemgetter(1)
from time import sleep
a1 = {'nome':'Mica','idade':17,'país':'Japão'}
print('\33[97:41m Vamos começar a ver o sistema de dicionários: \33[m')
sleep(0.81)
print('certo...')
sleep(0.27)
print(f'{a1.values()} = (\33[31m.values() \33[33m/Valores\33[m)')
print(f'{a1.keys()} = (\33[31m.keys() \33[33m/Chaves)\33[m')
print(f'{a1.items()} = (\33[31m.items() \33[33m/Todos os itens)\33[m')
sleep(0.81)
print(f'{a1["nome"]} mora no {a1["país"]}, e tem {a1["idade"]} anos.')
input('\33[31mNext:===>\33[m')
print('\33[31m.items()\33[m:')
for b1,b2 in a1.items():
 print(f'{b1} = {b2}')
input('\33[31mNext:===>\33[m')
del (a1['nome'])
print('\33[31mdel (v[''])\33[m:')
print('Esqueci um nome...')
input('\33[31mNext:===>\33[m')
a1['nome'] = 'Gustavo'
print('\33[31mv[""] = ""\33[m:')
print(f'''Era {a1["nome"]}?
\33[33mTalvez algum nome tenha sido apagado e adicionado
na minha lista...\33[m''')
a1['peso'] = 62.2
print(f'Essa pessoa pesava {a1["peso"]}? Deixa... estou louco.')
input('\33[31mNext:===>\33[m')
#
print('''Chega de brincar...
Vamos fazer uns dicionários com listas de países.''')
a2 = {'país':'Brasil','pib':'1,445 trilhão USD'}
a3 = {'país':'Estados Unidos','pib':'20,94 trilhões USD'}
a4=[]
a4.append(a2)
a4.append(a3)
for b3,b4 in enumerate(a4):
 print(f'{b3} - {b4["país"]}')
a5 = int(input('Digite qual país você quer ver o PIB: '))
#
a6=[]
a6.append(a2['pib']),a6.append(a3['pib'])
if a5<len(a6):
 print(f'O pib desse país, é: {a6[a5]}.')
print('\33[33mIsso foi só para lembra do enumerate()')
input('\33[31mNext:===>\33[m')
#
a7 = dict()
a8 = list()
for b3 in range(0,3):
 a7['estado'] = str(input('Nome do estado: '))
 a7['sigla'] = str(input('Sigla: '))
 a8.append(a7.copy())
for b4 in a8:
 for b5 in b4.values():
  print(f'{b5}',end=' ')
 print('')
print('\33[33mUsando o for como meio para entrar em listas e dicionários.')
input('\33[31mNext:===>\33[m')
#
print('\33[31mLinha de comando finalizada.\33[m')
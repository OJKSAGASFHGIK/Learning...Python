from operator import itemgetter
from random import randint
from time import sleep
#90:
print('\33[97:41m Ex:90 / Situação simples de média \33[m')
a1 = dict()
a2 = list()
a1['nome'] = str(input('Nome: '))
a1['média'] = float(input('Média: '))
print(f'''Nome: {a1['nome']}
Média: {a1['média']}''')
if a1['média'] > 5.9:
 print(f'Situação aprovada')
else:
 print(f'Situação reprovada')
input('\33[31mNext:===>\33[m')
#91: v2 = sorted(v1.items(),key=itemgetter(1),reverse=True)
print('\33[97:41m Ex:91 / Jogo de dados \33[m')
a2 = dict()
for b1 in range(4):
 a2[f'Jogador{b1+1}'] = randint(1, 6)
 print(f'Jogador{b1+1} = {a2[f"Jogador{b1+1}"]}')
 sleep(1)
a4 = sorted(a2.items(),key=itemgetter(1),reverse=True)
print('\33[32m+=-\33[m'*9)
for b2,b3 in enumerate(a4):
 print(f'\33[33m{b3[0]} com {b3[1]} - \33[31m{b2+1}¹ lugar\33[m')
input('\33[31mNext:===>\33[m')
#92: v1['key1','key2'] , v2['value1','value2'] , v3=dict , v3[v1[0]] = v2[0]
print('\33[97:41m Ex:92 / Aposentadoria \33[m')
a5 = str(input('Nome: '))
a6 = int(input('Ano de nascimento: '))
a7 = int(input('Número da carteira de trabalho(\33[31m0 = não tem\33[m): '))
if a7 != 0:
 a8 = int(input('\33[33mAno de contratação: '))
 a9 = float(input('Salário: \33[m'))
else:
 a8=a9=0
a10 = ['nome','nascimento','ctps','contratação','salário']
c1 = [a5,a6,a7,a8,a9]
a11 = dict()
for b4 in range(5):
 a11[a10[b4]] = c1[b4]
a12 = (a8-a6)+35
a11['aposentadoria'] = a12
print('\33[33m+=-\33[m'*9)
sleep(0.81)
print(f'\33[33m{a11["nome"]}\33[m nasceu em \33[33m{a11["nascimento"]}\33[m.')
if a8 == 0:
 sleep(0.81)
 print('\33[31mNão possui carteira de trabalho.\33[m')
else:
 sleep(0.81)
 print(f'O número do CTPS(carteira de trabalho), é: \33[33m{a11["ctps"]}\33[m')
 sleep(0.81)
 print(f'Foi contratado em \33[33m{a11["contratação"]}\33[m, recebendo: R$\33[33m{a11["salário"]:.2f}\33[m')
 sleep(0.81)
 print(f'Sua aposentadoria, será com \33[31m{a11["aposentadoria"]}\33[m anos.')
input('\33[31mNext:===>\33[m')
#93:
print('\33[97:41m Ex:93 / Gráfico de futebol \33[m')
a13 = dict()
a13['nome'] = str(input('Nome: '))
a14 = int(input('Quantas partidas: '))
a16 = list()
for b5 in range(1,a14+1):
 a15 = int(input(f'Quantos gols na ¹{b5} partida: '))
 a16.append(a15)
a13['gols'] = a16
a13['t.gols'] = sum(a16)
print('\33[33m+=-'*9)
sleep(0.81)
print(f'\33[31m{a13}')
print('\33[33m-=+\33[m'*9)
for b6,b7 in enumerate(a16):
 print(f'Na partida {b6+1}, fez: {b7}')
 sleep(0.81)
print(f'''\33[31m{a13["nome"]}\33[m, fez \33[31m{a13["t.gols"]}\33[m gols.
\33[33mEm {len(a16)} partidas.\33[m''')
input('\33[31mNext:===>\33[m')
#94:
print('\33[97:41m Ex:94 / Cadastro com listas e dicionários \33[m')
a17= dict()
b9= list()
b8= ''
while b8 != 'N':
 a17['Nome'] = str(input('Nome: '))
 while True:
  a17['Gênero'] = str(input('Gênero (\33[31mM/F/O\33[m): ')).upper()[0]
  if a17['Gênero'] in 'MFO':
   break
  print('Erro, digite um gênero (\33[33mM/F/O(Outro)\33[m):')
 a17['Idade'] = int(input('Idade: '))
 b9.append(a17.copy())
 a17.clear()
 b8 = str(input('Continuar (\33[31mS/N\33[m): ')).upper()

a18=a19= 0
for b10 in b9:
 a18 += b10['Idade']
 a19 += 1
a20= a18/a19
c2= list()
for b11 in b9:
 if b11['Idade'] > a20:
  c2.append(b11['Nome'])

c3 = list()
for b12 in b9:
 if 'F'in b12['Gênero']:
  c3.append(b12['Nome'])
sleep(0.81)
print(f'Total de cadastros: {len(b9)}')
print(f'Média: {a20:.2f}')
print(f'Acima da média: {c2}')
print(f'Todas as mulheres: {c3}')
sleep(2.43)
input('\33[31mNext:===>\33[m')
#95:
print('\33[97:41m Ex:95 / Desafio 93 com levantamentos \33[m')
d1 = ''
b13 = list()
c4 = dict()
c5 = list()
while d1 != 'N':
 a21 = str(input('Nome do jogador: '))
 a22 = int(input('Quantas partidas: '))
 c4['nome'] = a21
 for b14 in range(1,a22+1):
  b13.append(int(input(f'Gols na ¹{b14} partida: ')))
 c4['gols'] = b13[:]
 c5.append(c4.copy())
 b13.clear()
 c4.clear()
 d1 = str(input('Continuar? (S/N): ')).upper()[0]
print('\33[33m+=-\33[m'*9)
for b15,b16 in enumerate(c5):
 print(f'\33[31m{b15}\33[m. {b16["nome"]} = {b16["gols"]}')

a23 = -2
while a23 != -1:
 a23 = int(input('''De qual jogador, você quer ver o levantamento)? 
(\33[31m-1 para sair\33[m): '''))
 if a23 < len(c5) and a23 > -1:
  print('\33[31m+=-\33[m'*9)
  for b17,b18 in enumerate(c5[a23]['gols']):
   print(f'{b17}¹ jogo = {b18}')
input('\33[31mNext:===>\33[m')
#
print('\33[32m+=-'*9)
sleep(0.81)
print('\33[31mLINHA DE COMANDO FINALIZADA!!')
sleep(0.81)
print('\33[33m-=+'*9)
# a23 b18 c5 d1
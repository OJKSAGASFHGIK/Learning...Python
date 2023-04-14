from datetime import date
from time import sleep
def beautifulTitleR(title):
 print(f'\33[97:41m {title} \33[m')
 print('\33[31m=\33[m'*(len(title)+2))
def r(a1):
 return (f'\33[31m{a1}\33[m')
def m(a1):
 return (f'\33[35m{a1}\33[m')
def y(a1):
 return (f'\33[33m{a1}\33[m')
def next():
 input('\33[31mNext:===>\33[m')
def voto(a1):
 if 16 <= a1 < 18:
  print(f'Você possui a {r("idade mínima")} para votar.')
 elif a1 >= 18:
  print(f'É {r("muito requisitado")} sua participação na eleição.')
 else:
  print(f'Você {r("ainda não tem idade")} para votar.')
beautifulTitleR('Ex:101 / Voto')
a1 = int(input('Digite o ano de nascimento: '))
a2 = date.today().year-a1
voto(a2)
next()
beautifulTitleR('Ex:102 / Def simples e eficiente de fatorial')
def fatorial(a1,show=False):
 """
 :para a1: Recebe o valor a ser fatorado.
 :para show: Mostra todos os multiplicadores.
 :return: Resposta do valor recebido.
 """
 a2 = 1
 for b1 in range(a1,0,-1):
  a2*=b1
  if show == True:
   print(b1,end=' * ') if b1 != 1 else print(b1,end=' = ')
 return a2
print(fatorial(6,show=True))
print(m('Detalhe, essa def não precisa usar o segundo termo ;)'))
next()
beautifulTitleR('Ex:103 / Registrador de pontos(sem bugs{input com str})')
def ficha(a1='desconhecido',a2=''):
 if a1.isnumeric() or a1.strip() == '':
  a1 = 'desconhecido'
 else:
  a1 = a1.strip()
 if not a2.isnumeric() or a2.strip == '':
  a2 = 0
 print(f'Jogador(a) {r(a1)}, fez {r(a2)} ponto(s).')
a3 = str(input('Nome do jogador: '))
a4 = str(input('Quantidade de pontos: '))
ficha(a3,a4)
next()
beautifulTitleR('Ex:104 / Validando str para int(input com str)')
def ApenasNumeros(a1=''):
 a1 = str(input(a1))
 while True:
  if a1.isnumeric():
   a1 = int(a1)
   break
  else:
   a1 = str(input(f'{y("Erro! Digite um valor: ")}'))
 return a1
a1 = ApenasNumeros('Digite um valor: ')
print(f'{r(a1)} é um número.')
next()
beautifulTitleR('Ex:105 / Dicionários de notas')
def notas(*a1,sit=False):
 '''
 :para a1: Recebe notas
 :para sit: Classifica a média
 :return: Informações sobre as notas
 '''
 a2 = list()
 for b1 in a1:
  a2.append(b1)
 a3 = dict()
 a3['total de notas']=len(a2)
 a3['maior']=max(a2)
 a3['menor']=min(a2)
 a3['média']=sum(a2)/len(a2)
 if sit:
  if a3['média'] >= 7:
   a3['situação']='Média boa(5)'
  elif a3['média'] >= 5:
   a3['situação']='Dentro da média(5)'
  else:
   a3['situação']='Abaixo da média(5)'
 return a3
print(notas(3,7,3,7,sit=True))
next()
beautifulTitleR('Ex:106 / Help bonitinho(e atribuindo str a valores{break})')
def beautifulTitle(title='',color=0,line=True):
 """
 :param title: Título a ser escolhido
 :param color: Número da cor
 :param line: Com ou sem linha
 :return:
 """
 sC = ('\33[97:40m', '\33[97:41m', '\33[97:42m', '\33[97:43m', '\33[97:44m', '\33[97:45m', '\33[97:46m',
       '\33[97:47m', '\33[97:107m') #solid color
 print(f'{sC[color]} {title} \33[m')
 if line:
  print(f'\33[3{color}m=\33[m'*(len(title)+2))
def helpBonitinho():
 while True:
  beautifulTitle('Help na prática', 3)
  a1 = input('Digite o comando que você deseja saber(\33[31mfim\33[m): ')
  if str(a1) == 'fim':
   beautifulTitle('Fim',3,line=False)
   break
  print('\33[97:45m')
  help(a1)
helpBonitinho()
next()
print('\33[32m+=-'*9)
sleep(0.81)
print('\33[31mLINHA DE COMANDO FINALIZADA!!')
sleep(0.81)
print('\33[33m+=-'*9)
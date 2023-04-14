sC = ('\33[97:40m', '\33[97:41m', '\33[97:42m', '\33[97:43m', '\33[97:44m', '\33[97:45m', '\33[97:46m',
      '\33[97:47m', '\33[97:107m') #solid color

def beautifulTitle(title='',color=0,line=True):
 """
 :param title: Título a ser escolhido
 :param color: Número da cor
 :param line: Com ou sem linha
 :return:
 """
 global sC
 print(f'{sC[color]} {title} \33[m')
 if line:
  print(f'\33[3{color}m=\33[m'*(len(title)+2))


def beautifulTitle2(a1='',a2=0):
 global sC
 print(f'\33[3{a2}m========'*5)
 print(f'{sC[a2]}{a1:^40}\33[m')
 print(f'\33[3{a2}m========\33[m'*5)


def r(a1):
 return (f'\33[31m{a1}\33[m')


def options(*a1):
 for b1,b2 in enumerate(a1):
  print(f'\33[31m{b1+1} - \33[m{b2}')
 return a1


def cadastro(a1='Desconhecido(a)',a2=0,a3='lista'):
 try:
  a4 = open(f'{a3}.txt','at')
 except Exception as error:
  print(f'Erro: \33[34m{error.__class__}\33[m')
 else:
  a4.write(f'{a1};{a2}\n')


def listTXT(a1='lista'):
 try:
  a2 = open(f'{a1}.txt','rt')
 except:
  open(f'{a1}.txt','wt+')
 else:
  for b1 in a2:
   a3 = b1.split(';')
   a3[1] = a3[1].replace('\n','')
   print(f'{a3[0]:<27}Idade: {a3[1]}')
 finally:
  try:
   a2 = open(f'{a1}.txt','rt')
   if len(a2.read()) == 0:
    print('\33[34mNenhum cadastro...\33[m')
  except:
   print('\33[34mNenhum cadastro...\33[m')


def next():
 input('\33[31mNext:===>\33[m')
from urllib import request,error

def digiteInt(a1='Valor inteiro: '):
 while True:
  try:
   a2 = int(input(f'{a1}'))
  except:
   print('\33[34mDigite um valor inteiro...\33[m')
  else:
   break
 return a2


def digiteFloat(a1=0):
 while True:
  try:
   a2 = float(input(f'{a1}'))
  except:
   print('\33[34mDigite um valor inteiro ou decimal.\33[m')
  else:
   break
 return a2


def digiteDecimal(a1):
 while True:
  try:
   a2 = float(input(a1))
  except (ValueError,TypeError):
   print('Digite um valor decimal.')
  except Exception as error:
   print(f'Erro: \33[34m{error.__class__}\33[m')
  else:
   if a2 % 1 == 0 or a2 % 2 == 0 or a2 % 3 == 0 or a2 % 5 == 0 or a2 % 7 == 0:
    print('Digite um \33[34mvalor decimal\33[m.')
   else:
    break
 return a2


def digiteUrl(a1=''):
 try:
  a2 = str(input(a1))
  request.urlopen(a2)
 except error.URLError:
  print(f'URL inválida, ou incorreta.')
 else:
  print(f'A URL \33[31m{a2}\33[m é acessível.')
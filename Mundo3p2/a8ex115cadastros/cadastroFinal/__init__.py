from Mundo3p2.uteis.title import *
from Mundo3p2.uteis.debbugers import *


def cadastros(listas='lista'):
 while True:
  beautifulTitle2('Ex:115 / O que você deseja?',1)
  options('Novo cadastro','Ver cadastros','Sair')
  a1 = digiteInt('Qual sua opção: ')
  if a1 == 1:
   a1 = str(input('Nome: '))
   a2 = digiteInt('Idade: ')
   cadastro(a1,a2,listas)
  elif a1 == 2:
   beautifulTitle2('Lista',3)
   listTXT(listas)
  elif a1 == 3:
   beautifulTitle2('Obrigado, volte sempre!',4)
   break
  else:
   print('\33[34mDigite uma opção válida...\33[m')

#from datetime import datetime
# datetime.today().year
#from random import sample,randint
#from operator import itemgetter
# v2 = sorted(v1.items(),key=itemgetter(1),reverse=True)
#from time import sleep
#from urllib import request,error

#try: , except: , except Exception as v1: (v1.__class__) , else: , finnaly:
# except (ValueError,TypeError,ZeroDivisionError,KeyboardInterrupt):
# (Módulos de erros são úteis em erros imediatos de classe)

#int() , float() , str() , bool() , input()
#v1.isnumeric() , v1.isdigit() , v1 = int(v1) if v1.isnumeric() else ''

#if X condição X: elif: else:
# resposta if X condição X else resposta
#for V in range(9,0,-1): , enumerate()
#while X condição X:
#while True: , break
#v1 = 0 , += 1 , v1 += v2 , *= , -=

#tuple() = () , v.index(x) , v.count(x)
#list() = [] , .append(v1[:]) , .append(method(input())), .insert(n,x) , .pop() , .clear() ,
# .sort(reverse=True)
# (Você pode criar listas com inputs. Ex: v1 = ['',0])
#dict() = {} , v1['str'] = method(input()) , v1['str'] = max(v1) , .keys() , .values() , .items()
# , .copy()

#def function(v1): , global v1 , return v1 , """ """

#open(f'{v1}.txt','function(rt,wt+,at)')
# v1.write() , v1.read()

#.upper() , .lower()
#sorted() , len() , sum() , max() , min() , quit()
#\t , \n , end=''

#Notas sobre o gerenciamento de diretórios e pacotes:
# Right click >> New >> Directory
# Right click >> New >> Python Package

# Resumidamente, para você exportar um módulo para dentro de um módulo
# principal, você primeiro precisa de uma Python Package.

# Para navegar entre as pastas, você vai usar . para entrar de pasta em
# pasta. Quando você importar a sua Package, a package é importada
# inteiramente, junto ao arquivo __init__.py .

# O arquivo __init__.py é o que vai armazenar suas defs/módulos. É esse
# arquivo, que define se um programa é um diretório ou um pacote, então
# é vital que esses arquivos fiquem organizados para não acionar bugs.

# from directory.package import fuction/def
# from directory.package import *
#https://www.youtube.com/watch?v=etjJ_4Eqrk8
#Teórica e prática:
# 5:20 - help() , 7:02 - quit , 7:25 - help(method) , method(method.__doc__)
# 9:12 - 'O que são as "docstrings"?' , 14:17 - """""" (explicando uma def{docstring}) ,
# 18:17 - def function(v1=0,v2=0,v3=0): (parâmetros opcionais) , 21:02 - function(v3=1 + v2=3) ,
# 21:46 - 'Escopo de variáveis' , 22:28 - 'variável global(uma def pode conter uma variável)' ,
# 23:15 - 'variável local(a variável de uma def não pode ser reutilizada)' , 27:08 - 'variáveis
# iguais, podem ter valores diferentes, dentro e fora de uma def' , 30:11 - global v ,
# 31:39 - 'Retornando valores' , 33:07 - return v , 37:44 - return True
# a5 def: a7 b2
from time import sleep
def next():
 """To usando essa def simples para pular de exercício em exercício,
 de maneira cadenciada."""
 input('\33[31mNext:===>\33[m')
 '''To usando essa def simples para pular de exercicio em exercicios,
 de maneira cadenciada.'''
def r(aa1):
 return (f'\33[31m{aa1}\33[m')
def gree(aa2):
 return (f'\33[32m{aa2}\33[m')
def y(aa3):
 return (f'\33[33m{aa3}\33[m')
def blu(aa4):
 return (f'\33[34m{aa4}\33[m')
def m(aa5):
 return (f'\33[35m{aa5}\33[m')
def c(aa6):
 return (f'\33[36m{aa6}\33[m')
def grey(aa7):
 return (f'\33[37m{aa7}\33[m')
def w(aa8):
 return (f'\33[97m{aa8}\33[m')
while True:
 a1 = str(input('''Deseja ver para que serve algum método?
(\33[31mS/N\33[m): ''')).upper()[0]
 print('\33[31m===\33[m'*9)
 if a1 == 'S':
  help(input('\33[31mDigite um método para explicar: \33[m'))
 elif a1 == 'N':
  print('''Você também pode usar o \33[31mhelp()\33[m no prompt,
e para sair, você usa o comando \33[31mquit\33[m.''')
  break
 else:
  print('\33[33mDigite uma opção valida.\33[m')
next()
print('Sobre a def \33[31mnext()\33[m:')
help(next)
print('Isso é o que chamamos de \33[33mdocstring\33[m, uma explicação da def(comentário).')
print('Você também pode obter uma explicação usando print(função\33[35m.__doc__\33[m).')
next()
def sumAll(*a3):
 a2 = a3
 a4=0
 for b1 in a2:
  a4+=b1
 return(a4)
print('''Aqui a gente vê, que o def function(\33[35m*\33[mv1) ,
funciona com vários valores.''')
a2 = sumAll(3,9,27,81)
print(f'O resultado da soma, é: \33[31m{a2}\33[m')
next()
print('''Agora você vai ver resultados, que não precisam estar completos na def.
Usando def function(v1\33[35m=0\33[m,v2\33[35m=0\33[m), como:''')
sleep(2.43)
def sum3Numbers(a5=0,a6=0,a7=0):
 b2 = a5+a6+a7
 return(b2)
a3 = sum3Numbers()
print(f'A resposta {a3}. (\33[32msem elementos\33[m)')
sleep(0.81)
a4 = sum3Numbers(3)
print(f'A resposta {a4}. (\33[32mcom 1 elemento\33[m)')
sleep(0.81)
a5 = sum3Numbers(3,3,3)
print(f'E a resposta {a5}. (\33[32mcom 3 elementos\33[m)')
sleep(2.43)
print('''E a gente percebe que o \33[35m=0\33[m, possibilita a ausência de valores.
\33[33mSão parâmetros opcionais, porque o valor foi atribuido a \33[31m0\33[m.''')
next()
# sleep , colors
def ValoresDiferentesDe0(a8=0,a9=0):
 print(f'{y("Por exemplo, se os valores fossem:")} a8={m(a8)}, e a9={m(a9)}.')
 sleep(1.62)
 print(f'O resultado da soma, seria:',end=' ')
 a10 = a8 + a9
 print(f'{r(a10)}')
 sleep(1.62)
 print(f'Isso acontece dentro dos parênteses da def.')
a8 = int(input(f'{m("1¹")} valor: '))
a9 = int(input(f'{m("2¹")} valor: '))
ValoresDiferentesDe0(a8=a8,a9=a9)
next()
# colors
a6 = int(input('N: '))
def escopoGlobal():
 a6 = 243
 print(f'Seu número foi alterado para {r(a6)}. Como um escopo global.')
escopoGlobal()
next()
# colors
def escopoLocal(a11):
 print(f'Seu número ainda é {r(a11)}. E é um escopo local.')
a7 = int(input('N: '))
escopoLocal(a7)
next()
print(m('''Você pode ter variáveis iguais, com valores diferentes,
dentro e fora de uma def.'''))
next()
def escopoGlobalUsandoOGlobal():
 global a6
 print(f'''De qualquer, a gente pode pegar aquele seu primeiro valor la,
usando um comando chamado {m("global")}, e sabemos que ele é: {r(a6)}.''')
next()
print(f'Agora vamos ver um comando simples com {m("True")} e {m("False")}.')
next()
def pair(a12):
 a13 = True if a12 % 2 == 0 else False
 return a13
a8 = int(input('Digite um valor: '))
if pair(a8):
 print(f'{m(a8)} é {r("par")}.')
else:
 print(f'{m(a8)} é {r("ímpar")}.')
next()
print(r("LINHA DE COMANDO FINALIZADA!!"))
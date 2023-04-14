#https://www.youtube.com/watch?v=xz2B3bfNjEk
# 9:50 - line 1 ,  11:27 - (erro de valor{ValueError}) ,
# 13:07 - (não pode ser dividido por zero{ZeroDivisionError}) ,
# 14:05 - (PHP e JavaScript aceitariam{TypeError}) ,
# 14:58 - (listas e repetições começam por 0{IndexError}) ,
# 15:40 - (modulo inexistente{ModuleNotFoundError}) , 16:05 - (python Exception list) ,
# 17:20 - try: \ except: , 19:31 - else: , 20:21 - finally: , 21:13 except Exception as v1:
# v1.__class__
#Exercícios:
# continue , * (importa tudo) , v2 = open(v1, 'rt') (mantem o arquivo aberto) , v2 = open(v1, 'wt+')
# (cria o arquivo, o + serve para criar) , v2 = open(v1,'at') (adiciona ao texto) \ v1.write() ,
# v1.read() (exibi oq está dentro) , v1.close()
from beautifulTitle import beautifulTitle,next
from time import sleep
beautifulTitle('Tratamento de erros e exceções',1)
beautifulTitle('except',line=False)
try:
 a1 = int(input('Numerador: '))
 a2 = int(input('Denominador: '))
 a3 = a1 / a2
except:
 print('Resultado inválido.')
else:
 print(f'O resultado da divisão, é: {a3}')
finally:
 sleep(0.81)
 print('Nota: Resultados \33[33mnão ficam declarados\33[m dentro dessas condições.')
 print('Também não podemos nos esquecer do \33[35mfinally:\33[m.')
 sleep(0.27)
next()
beautifulTitle('except Exception as v1 \ v1.__class__',line=False)
try:
 a1 = int(input('Numerador: '))
 a2 = int(input('Tente digitar \33[35m0\33[m: '))
 a3 = a1/a2
except Exception as error:
 print(f'Resultado inválido. Erro: \33[34m{error.__class__}\33[m')
else:
 print(f'O resultado da divisão, é: {a3}')
next()
beautifulTitle('except (ValueError,TypeError,ZeroDivisionError,KeyboardInterrupt):',line=False)
while True:
 try:
  a1 = int(input('Numerador: '))
  a2 = int(input('Tente digitar \33[35mstring,0,\33[33m ou até mesmo nada\33[m: '))
  a3 = a1 / a2
 except (ValueError,TypeError):
  print('Digite um valor numérico')
 except ZeroDivisionError:
  print(f'Não pode ser dividido por \33[35m0\33[m.')
 except KeyboardInterrupt:
  print('O usuário preferiu não digitar nada.')
 except Exception as error:
  print(f'Erro: \33[34m{error.__class__}\33[m')
 else:
  print(f'O resultado é: \33[31m{a3}\33[m')
  break
print('\33[31mLinha de comando finalizada! ;)\33[m')
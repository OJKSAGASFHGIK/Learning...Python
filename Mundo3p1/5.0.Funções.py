#https://www.youtube.com/watch?v=ezfr9d7wd_k&t=442s
#Teórica:
# 8:34 - (pra que servem as funções , rotina!) , 9:32 - def função(): print('---') ,
# 10:28 - (def na prática) , 15:50 - def função(fun): print(fun) / fun('parâmetro') ,
# 30:30 - def(*) (desempacotamento {para casos sem lista}) .
#Prática:
# flush=True
# a3 b1 aa5 bb2
from time import sleep
def lineY():
 print('\33[33m+=-\33[m'*9)
def r(red):
 print(f'\33[31m{red}\33[m')
def next():
 input('\33[31mNext:===>\33[m')
def soma(aa1,aa2):
 bb1=aa1+aa2
 print(f'A soma de \33[33maa1={aa1}\33[m + \33[33maa2={aa2}\33[m é igual a \33[31mbb1={bb1}\33[m.')
def beautifulTitleR(title):
 print('\33[33m==='*9)
 print(f'\33[97:41m {title} \33[m')
 print('\33[33m==='*9,'\33[m')
def sumAll(*all):
 aa3 = 0
 for bb2 in all:
  aa3 += bb2
 print(f'A soma de todos os valores, é: {aa3}')
def doubleList(aa4):
 aa5 = 0
 while aa5 < len(aa4):
  aa4[aa5] *= 2
  aa5 += 1
 print(aa4)

lineY()
r('A cor foi mudada usando uma def')
lineY()
sleep(0.81)

next()
a1 = 2
a2 = 3
soma(aa1=a2,aa2=a1)
sleep(0.81)

next()
beautifulTitleR('Esse é um título bonito')
sleep(0.81)

next()
sumAll(3,9,27,81)
sleep(0.81)

next()
print(f'\33[33mLista padrão: \33[m[3,9,27,81]')
a3 = [3,9,27,81]
r('Lista com números dobrados:')
doubleList(a3)
sleep(0.81)
print('\33[32m+=-'*9)
r('LINHA DE COMANDO FINALIZADA!!')
print('\33[33m-=+'*9)
from Mundo3p2.uteis.title import beautifulTitle, next, r
from Mundo3p2.uteis.debbugers import digiteFloat
from Mundo3p2.uteis.moeda import coinResume
from time import sleep
beautifulTitle('Ex:107-112 / Módulos de conversão em moeda',1)
a1 = digiteFloat(f'Digite um valor, {r("R$")}: ')
coinResume(a1,110,10)
next()
print('\33[32m+=-'*9)
sleep(0.81)
print('\33[31mLINHA DE COMANDO FINALIZADA!!')
sleep(0.81)
print('\33[33m-=+'*9)
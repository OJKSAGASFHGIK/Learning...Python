from Mundo3p2.uteis.debbugers import digiteInt,digiteDecimal,digiteUrl
from Mundo3p2.uteis.title import beautifulTitle,next
from time import sleep
beautifulTitle('Ex:113 / Apenas inteiro e decimal',1)
a1 = digiteInt('Digite inteiro: ')
a2 = digiteDecimal('Digite decimal: ')
print(f'\33[31m{a1}\33[m é inteiro, e \33[31m{a2}\33[m é decimal.')
next()
beautifulTitle('Ex:114 / Validador de link',1)
digiteUrl('Digite um link: ')
next()
print('\33[32m========='*3)
sleep(0.81)
print('\33[31mLINHA DE COMANDO FINALIZADA!!')
sleep(0.81)
print('\33[33m========='*3)
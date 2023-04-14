#\33[m
#style: 0=none, 1=bold, 4=underline, 7=negative
#text: 30=black, 31=red, 32=green, 33=yellow, 34=blue, 35=magenta, 36= cyan,
# 37=grey, 97=white
#background: 40=black, 41=red, 42=green, 43=yellow, 44=blue, 45=magenta,
# 46=cyan, 47=grey, 107=white
#revisar: x
from random import sample
from operator import itemgetter
from datetime import datetime
a10 = dict()
a11 = list()
for b3 in range(3):
 a10['a'] = int(input('N: '))
 a11.append(a10.copy())
print(a11)

input('Next:-->')
a8 = {'a':3,'b':9,'c':27}
a9 = sorted(a8.items(),key=itemgetter(1),reverse=True)
print(a9)

input('Next:-->')
print(datetime.today().year)

input('Next:-->')
a7 = [3,9,27]
for b2 in range(len(a7)):
 print(a7[b2])

input('Next:-->')
a6 = [3,9,27]
a6.clear()
print(a6)

input('Next:-->')
a5 = []
a5.insert(3,'a')
a5.insert(0,'b')
print(a5)
print(a5[1])

input('Next:-->')
a4 = [3,9,27]
a4.sort(reverse=True)
print(a4)

input('Next:-->')
print('\33[97:41m Rascunho: Tuplas \33[m')
a3 = ('pedra','pena')
for b1 in a3:
 print(f'{b1}:',end=' ')
 for b2 in b1:
  if b2.lower() in 'aeiou':
   print(b2,end='')
 print()

input('Next:-->')
a2 = tuple(sample(range(1,10),6))
a2 = sorted(a2)
print(a2)

input('Next:-->')
a1 = [3,9,27]
print(a1)
print(a1.index(9)+1)
del a1[1]
print(a1[int(input('hm? '))])

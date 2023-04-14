#https://www.youtube.com/watch?v=LH6OIn2lBaI&t=12s
#Teórica:
#4:54, 5:49, 6:09, 6:22, 7:51, 9:09, 10:29, 12:20, 13:07, 13:38,
# 14:29.
#Prática:
#16:17, 19:15, 19:37, 19:48, 20:08, 20:51, 22:10, 22:58, 23:25, 23:59, 24:35
# 25:15.
#a2
a1 = 1
while a1 < 4+1:
 a2 = int(input('Repetição simples com while: '))
 a1 += 1
print('\33[31m-End\33[m')
input('\33[31m-Next:==>\33[m')
#
a3 = 1
while a3 != 0:
 a4 = int(input('Enquanto você digitar um número diferente de 0... : '))
print('\33[31m-End(isso ai é uma flag)\33[m')
input('\33[31m-Next:==>\33[m')
#
a4 = 'S'
while a4 == 'S':
 a5 = int(input('Digite um valor: '))
 a4 = str(input('Quer continuar? [\33[31mS\33[m] : ')).upper()
print('\33[31m-End(isso ai é uma flag com string)\33[m')
input('\33[31m-Next:==>\33[m')
#
a6 = 1
a7 = a8 = 0
while a6 != 0:
 a6 = int(input('Digite um valor: '))
 if a6 != 0:
  if a6 % 2 == 0:
   a7 += 1
  else:
   a8 += 1
print(f'''Pares: {a7}
Ímpares: {a8}''')
#
print('''\33[31m-End(if não é uma estrutura de repetição. Cortando o
0 no final. Segregando os números perfeitamente.\33[m''')
input('\33[31m-Next:==>\33[m')
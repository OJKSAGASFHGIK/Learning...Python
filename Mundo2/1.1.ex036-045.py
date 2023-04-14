from datetime import date
from time import sleep
from random import randint
#36: (atenuar se necessário)
a1 = float(input('Qual o valor da casa/terreno? R$: '))
a2 = float(input('Salário do comprador; R$: '))
a3 = float(input('Em quantos anos de financiamento? '))
#Condição: A prestação não pode exceder 30% do salário.
b1 = a1/(a3*12) # prestação
b2 = a2*0.30 # 30% do salário
if b1<=b2:
 print(f'-A casa pode ser financiada em {a3:.0f} anos.')
 print(f'''Seu salário excede o valor da prestação bancária
 (dentro de 30%({b2:.2f}), sobra: R$ +{b2-b1:.2f})
 Prestação: R${b1:.2f}''')
else:
 print(f'-A casa não pode ser financiada em {a3:.0f} anos.')
 print(f'''Seu salário não excede o valor da prestação bancária
 (dentro de 30%({b2:.2f}), falta: R$ {b2-b1:.2f})
 Prestação: R${b1:.2f}''')
input('NEXT -> ')
#37: .bin() , .oct() , .hex()
a4 = int(input('Digite um número para conversão: '))
print('(1) Binário\n(2) Octal\n(3) Hexadecimal')
a5 = str(input('Digite sua opção: '))
if '1'in a5:
 print(f'{a4} = \33[31m{bin(a4)[2:]}\33[m (binário)')
elif '2'in a5:
 print(f'{a4} = \33[31m{oct(a4)[2:]}\33[m (octal)')
elif '3'in a5:
 print(f'{a4} = \33[31m{hex(a4)[2:]}\33[m (hexadecimal)')
else:
 print('\33[33mOpa, eu não ti dei essa opção... :/\33[m')
input('NEXT -> ')
#38:
a6 = float(input('Primeiro número: '))
a7 = float(input('Segundo número: '))
if a6>a7:
 print('\33[31mO primeiro é maior.\33[m')
elif a7>a6:
 print('\33[31mO segundo é maior.\33[m')
elif a6==a7:
 print('\33[32mOs dois são iguais.\33[m')
input('NEXT -> ')
#39: from datetime import date , date.today().year (atenuar se necessário)
print('\33[4:32mEntrada estudantil\33[m')
a8 = int(input('Ano de nascimento da criança: '))
a9 = date.today().year
b3 = a9-a8 #ano de entrada
if b3 == 3:
 print(f'Seu filho está no {b3}¹ ano:')
 print('E está no tempo de entrada para os estudos.')
elif b3 < 3:
 b4 = 3-b3
 print(f'Seu filho ainda não está no tempo de introdução aos estudos.')
 print(f'Falta {b4} ano(s).')
elif b3 > 3:
 b4 = b3-3
 print(f'Seu filho já passou do tempo de introdução aos estudos.')
 print(f'E está atrasado {b4} ano(s).')
input('NEXT -> ')
#40:
print('\33[97:42m Média escolar \33[m')
a10 = float(input('Nota do 1¹ bimestre: '))
a11 = float(input('Nota do 2¹ bimestre: '))
b5 = (a10+a11)/2
if b5<5:
 print(f'''O aluno está com a média baixa dentro de
 \33[32m{b5:.2f}\33[m pontos.''')
 print('Será necessario fazer uma \33[32mrecuperação\33[m.')
elif b5>=5 and b5<7:
 print(f'''O aluno está com a média passável dentro de
 \33[33m{b5:.2f}\33[m pontos.''')
elif b5>=7:
 print(f'''O aluno está com a média boa dentro de 
 \33[31m{b5:.2f}\33[m pontos!''')
input('NEXT -> ')
#41:
print('\33[97:41m Confederação Nacional De Natação \33[m')
a12 = int(input('Qual ano de nascimento: '))
b6 = date.today().year-a12
if b6<=9:
 print(f'''Você tem {b6} anos.
-Até \33[31m9\33[m anos, sua categoria é mirim.''')
elif b6>9 and b6<=14:
 print(f'''Você tem {b6} anos.
-Até \33[31m14\33[m anos, sua categoria é infantil.''')
elif b6>14 and b6<=19:
 print(f'''Você tem {b6} anos.
-Até \33[31m19\33[m, sua categoria é junior.''')
elif b6>19 and b6<=25:
 print(f'''Você tem {b6} anos.
-Até \33[31m25\33[m, sua categoria é sênior.''')
else:
 print(f'''Você tem {b6} anos.
-Com mais de \33[31m25\33[m, sua categoria é master.''')
input('NEXT -> ')
#42:
print('\33[97:43m Cálculos com triângulos \33[m')
a13 = float(input('Primeiro lado: '))
a14 = float(input('Segundo lado: '))
a15 = float(input('Terceiro lado: '))
if a13<a14+a15 and a14<a13+a15 and a15<a13+a14:
 print('Esse é um triângulo',end=' ')
 if a13 == a14 == a15:
  print('equilátero.')
 elif a13 != a14 != a15 != a13:
  print('escaleno.')
 else:
  print('isósceles.')
input('NEXT -> ')
#43
print('\33[7:37:107m IMC \33[m')
a16 = float(input('Peso: '))
a17 = float(input('Altura: '))
b7 = a16/(a17**2)
if b7<=18.5:
 print(f'Seu IMC, é: {b7:.2f}\nE você está abaixo do peso.')
elif b7<=25:
 print(f'Seu IMC, é: {b7:.2f}\nE você está no peso ideal.')
elif b7<=30:
 print(f'Seu IMC, é: {b7:.2f}\nE seu peso está um pouco acima do ideal.')
elif b7<=40:
 print(f'Seu IMC, é: {b7:.2f}\nVocê tem obesidade. Procure assistência.')
else:
 print(f'''Seu IMC é: {b7:.2f}Você tem obesidade mórbida.
 Procure assistência profissional.''')
input('NEXT -> ')
#44
print('\33[30:44m Loja de informática \33[m')
a18 = float(input('\33[31m Valor total: \33[m'))
a19 = input('''[\33[33m1\33[m] - À vista (dinheiro/cheque)
\33[31m10% de desconto\33[m
[\33[33m2\33[m] - À vista (no cartão)
\33[31m5% de desconto\33[m
[\33[33m3\33[m] - Em até 2x no cartão
[\33[33m4\33[m] - 3x ou mais no cartão...
\33[34m20% de juros\33[m
Forma de pagamento: ''')
b8 = a18*0.90
b9 = a18*0.95
b10 = a18*1.20
if '1'in a19:
 print(f'Sua compra vai sair por {b8:.2f}, com 10% de desconto.')
elif '2'in a19:
 print(f'Sua compra vai sair por {b9:.2f}, com 5% de desconto.')
elif '3'in a19:
 c1 = a18/2
 print(f'''Sua compra em 2 vezes, vai sair por {c1:.2f} mensais.
Totalizando: {a18:.2f}''')
elif '4'in a19:
 a20 = int(input('Em quantas vezes: '))
 c2 = (b10/a20)
 print(f'''Sua compra em {a20} vezes, vai sair por {c2:.2f} mensais,
com 20% de juros. Totalizando: {b10:.2f}''')
else:
 print('Opção inválida.')
input('NEXT -> ')
#45: from time import sleep
print('''[\33[31m0\33[m] - Pedra
[\33[31m1\33[m] - Papel
[\33[31m2\33[m] - Tesoura''')
a21 = int(input('Sua opção: '))
a22 = randint(0,2)
a23 = ('Pedra','Papel','Tesoura')
if a21!=0 and a21!=1 and a21!=2:
 print(f'Não temos essa opção ;-;')
 quit()
print('\33[1:97:42m JO \33[m')
sleep(0.5)
print('\33[1:97:43m KEN \33[m')
sleep(1)
print('\33[1:97:41m PÔ!! \33[m')
print('\33[33m+-\33[m'*9)
print(f'''Player: {a23[a21]}\nComputador: {a23[a22]}''')
print('\33[32m+-\33[m'*9)
if a22==0: #Computador = pedra
 if a21==0:
  print('Empate...')
 elif a21==1:
  print('Você venceu!')
 elif a21==2:
  print('Você perdeu!')
elif a22==1: #Computador = papel
 if a21==0:
  print('Você perdeu!')
 elif a21==1:
  print('Empate...')
 elif a21==2:
  print('Você venceu!')
elif a22 == 2: #Computador = tesoura
 if a21==0:
  print('Você venceu!')
 if a21==1:
  print('Você perdeu!')
 if a21==2:
  print('Empate...')
input('NEXT -> ')
print('\33[33m=-\33[m'*18)
print('\33[31m LINHA DE COMANDO FINALIZADA!! \33[m')
print('\33[33m=-\33[m'*18)
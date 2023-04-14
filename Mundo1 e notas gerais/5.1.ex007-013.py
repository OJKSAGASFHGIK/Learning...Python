#Média escolar:
print('-Média escolar:')
a = input('Nome do aluno: ')

a2 = float(input('Nota do 1¹ bimestre: '))
print(f'Média até o momento: {a2}')
a3 = float(input('Nota do 2¹ bimestre: '))
print(f'Média até o momento: {(a2+a3)/2}')
a4 = float(input('Nota do 3¹ bimestre: '))
print(f'Média até o momento: {(a2+a3+a4)/3}')
a5 = float(input('Nota do 4¹ bimestre: '))
print(f'Média final: {(a2+a3+a4+a5)/4:.1f}')
print(27*'=')
input('Confirmar?')
print(27*'=')
#Conversão de unidades de medida:
print('-Conversão de unidades de medida:')
a6 = float(input('Quantos metros você tem? '))
b1 = a6*1000
b2 = a6*100
b3 = a6*10
b4 = a6/10
b5 = a6/100
b6 = a6/1000
print('Você possui:')
print(f'{b1:.0f} milímetros.\n{b2:.0f} centímetros.\n{b3:.1f} decímetros')
print(f'{b4} decâmetros.\n{b5} hectômetros.\n{b6} quilômetros.')
input('Confirmar?')
print(27*'=')
#Tabuada:
print('-Tabuada:')
a7 = int(input('Escolha um número: '))
print(f'{a7} *1= {a7*1}\n{a7} *2= {a7*2}')
print(f'{a7} *3= {a7*3}\n{a7} *4= {a7*4}')
print(f'{a7} *5= {a7*5}\n{a7} *6= {a7*6}')
print(f'{a7} *7= {a7*7}\n{a7} *8= {a7*8}')
print(f'{a7} *9= {a7*9}\n{a7}*10= {a7*10}')
input('Confirmar?')
print(27*'=')
#Converting coin:
print('-Converting coin.')
a8 = float(input('How much dollars do you need? '))
print(f'You need R$ {a8*4.70:.2f}.')
input('Confirmar?')
print(27*'=')
#Quantos litros de tinta vc precisa.
print('Quantos litros de tinta vc precisa... ?')
a9 = float(input('Qual altura? ' ))
a10 = float(input('Qual a largura? '))
b7 = (a9*a10)/2
print(f'Sua parede tem: {a9*a10:.2f}m²')
print(f'Você precisa de {b7:.2f}L de tinta.')
input('Confirmar?')
print(27*'=')
#Porcentagens com produtos e salários.
a11 = float(input('Qual o preço do produto? R$'))
b8 = a11-(a11*0.05)
print(f'Esse produto, de: R${a11:.2f}')
print(f'Ficará por: R${b8:.2f} (5% de desconto)')
print('-Linha de comando finalizada.')
input('Confirmar?')
print(27*'=')
a12 = input('Qual o nome do funcionário? ')
a13 = float(input(f'Qual o salário de {a12}? R$'))
b9 = a13+(a13*0.15)
print(f'{a12} ganhava R${a13:.2f},e agora ganhará: R${b9:.2f}.')
print('Um acrescento de 15%.')
print(27*'=')
print('Linha de comando finalizada.')
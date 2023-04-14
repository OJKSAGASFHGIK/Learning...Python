#TXT em lista vazia ou sem arquivo TXT:
# finally:
#  try:
#   v2 = open(f'{v1}.txt', 'rt')
#   if len(v2.read()) == 0:
#    print('\33[34mNenhum cadastro...\33[m')
#  except:
#   print('\33[34mNenhum cadastro...\33[m')

#Organizando arquivos TXT em listas demonstrativas:
# for b1 in v2:
#  v3 = b1.split(';')
#  v3[1] = v3[1].replace('\n', '')
#  print(f'{v3[0]:<27}Idade: {v3[1]}')

#v2 += v1.index(max(v1))

# def...
#  a1 = ''
#  while a1 != 'N':
#   a1 = str(input('(S/N): ').upper())
#   if a1 == 'S':
#    print('Uma condição se aplica.')
#   elif a1 != 'N':
#    print('\33[33mDigite uma opção válida.\33[m')

#v2 = str(input(v1)).replace(',','.').strip()

#Transformando comandos em str(para finalizar inputs{bugs}):
#if str(v1) == 'str':
# break

#Troca de cores para defs e meios gerais:
#v1 = str(input('c: '))
#print(f'\33[{v1}m')

#(princípio)comparador de par e impar:
#v1 % 2 == 0

#(princípio)comparador maior e menor:
#???

#média perfeita:
#a24 = [0,0]
#for b in range(0,2):
# a24[b] = int(input('Nota: '))
#print(sum(a24)/len(a24))

#fatorial:
#a1 = int(input('N: '))
#a2 = 1
#for b1 in range(a1,0,-1):
# a2*=b1
# print(a2)
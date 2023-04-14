#Aninhamento complexo:
#Uma coisa que ainda não mencionei aqui, foi a junção do for com if,
# mas vou deixar uma mini base aqui. E ela é:
#  for a in range(0, 8+1):
#   if b
#    resultado
#   variável
#   variável
#Questões com for:
#==
for a in range(0, 4+1):
 print('Str repetida.')
input('NEXT:==')
#===
for a in range(20, 15-1, -1):
#Aqui vemos que o último número dentro de uma formatação, não se refere
# exclusivamente a intercalação, e sim, a uma iteração que também pode
# servir para jogar resultados de trás pra frente.
#Outra coisa a si notar, é que o -1 no 'número final', nesse caso, também
# serve para ordenar, só que de maneira diferente, que seria usar o '+1'.
 print(a)
input('NEXT:==')
#===
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Intercalações: '))
for d in range(a, b+1, c):
#Aqui conseguimos ver como funciona a ordem de formatação numérica.
# (dentro de um for)
 print(d)
input('NEXT:==')
#===
a = int(input('Número: '))
for b in range(0, a+1, 2):
#Você pode sempre usar o +1 no número final.
# (para ter o final exato)
 print(b)
input('NEXT:==')
#===
a = int(input('Número: '))
b = 0
for c in range(0, a):
# in range(1:1:1) serve para definir quantidade e ordem.
# Um input se repete dentro de um for.
 b += 1
# b vai ter um resultado atribuído no final.
 print(b)
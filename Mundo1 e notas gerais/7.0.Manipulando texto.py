#Todos os comandos demonstrados:
#Fatiamento:
# (v[::])
# Análize:
# len(v) , v.count('str') , v.find('str') , 'str'in v
#Transformação:
# v.replace('str','str desejada') , v.upper() , v.lower() , v.capitalize()
# v.title() , v.strip() , v.lstrip() , v.rstrip()
#Divisão:
# v.split()
#Junção:
# 'str'.join(v)
#Fatiamento:
# "O fatiamento simples, corta até a "penúltima" letra."
a1 = 'Essa frase foi fatiada:'
print('string = Essa frase foi fatiada')
print('print(a1[0:15])')
print('a1 -',a1[0:15])
input('Enter:===')
# "O comando com "1:1:1", segue uma ordem, que é:
# início : fim : e intercalações
# Caso não haja especificação para inicio ou final de string:
# 1::2 = Ele vai escolher a 1¹ letra "até o final"(intercalando 2).
# Nota: "A primeira letra é sempre 0¹"
# Ex:
a2 = 'Essa frase foi fatiada intercalando 1 letra até o final:'
print('string = Essa frase foi fatiada intercalando 1 letra até o final:')
print('print(a2[1::2])')
print('a2 -',a2[1::2])
input('Enter:===')
#Análize: len(variável)
a3 = 'A quantidade de caractéres foi contada:'
print('string = A quantidade de caractéres foi contada:')
print('print(len(a3))')
print('a3 - Quantidade de caracteres =',len(a3))
input('Enter:===')
#variável.count('string')
a4 = 'A string foi contada usando .count :'
print('string = A string foi contada usando .count :')
print('print(a4.count(a(<<string),0,27))')
print('a4 - essa string possui',a4.count('a',0,21), 'letras "a".')
input('Enter:===')
#variável.find('string')
a5 = 'Encontre o AMONGUS'
print('string = Encontre o AMONGUS')
print('print(a5.find(AMONGUS(<<string)))')
print('a5 - Vc encontrou AMONGUS na casa:',a5.find('AMONGUS'))
print('Se a string não for encontrada, o resultado será: -1')
input('Enter:===')
#'string'in variável
print('Dentro de "Olá Hatsune!":')
print('Existe a palavra "Olá"?')
a6 = 'Olá Hatsune!'
print('E a resposta, é:',('Olá'in a6))
input('Enter:===')
#Transformação: variável.replace('string','string desejada')
print('Essa frase vai trocar a palavra biscoito.')
a7 = 'Essa frase vai trocar a palavra biscoito.'
print(a7.replace('biscoito','cookie'))
input('Enter:===')
#variável.upper() , variável.lower()
print('VAI FICAR tudo maiúsculo!')
a8 = 'VAI FICAR tudo maiúsculo!'
print(a8.upper())
a9 = a8.replace('maiúsculo','minúsculo')
print(a9.lower())
input('Enter:===')
#variável.capitalize()
a10 = 'eSSE TEXTO, FICOU NORMAL.'
print(a10.capitalize())
input('Enter:===')
#variável.title()
a11 = 'toda primeira letra maiúscula.'
print(a11.title())
input('Enter:===')
#variável.strip() , variável.lstrip() , variável.rstrip()
a12 = '   Os espaços dos foram retirados.   '
print(a12.strip(), '(nos dois cantos.)')
print(a12.lstrip(), '(na esquerda)')
print(a12.rstrip(), '(na direita)')
input('Enter:===')
#Divisão: variável.split() , #Junção: 'str'.join(variável)
a13 = 'Essa frase foi splitada e modificada entre os espaços.'
print(a13.split())
b1 = a13.split()
print('='.join(b1))
input('Enter:===')
#Extra:
#Junção de comandos: v.lower().count('str')
print('ESsa É UMA JUNçãO dE CoMandos.')
a14 = 'ESsa É UMA JUNçãO dE CoMandos.'
print('E possui',a14.lower().count('s') ,'letras "s".')
input('Enter:===')
#v.lower().find('str')
a15 = 'A palavra COokie foi encontrada na casa'
print((a15), a15.lower().find('cookie'),'.')
input('Enter:===')
#Interações úteis com "v.split()"
a16 = 'É, eu não dou o cu.'
b2 = a16.split()
print(b2[3::],b2[0],b2[3][1],b2[5][1])
input('Enter:===')
#Mesma variável.
a17 = 'Você usou uma variável diferente, para modificar uma palavra.'
a17 = a17.replace('diferente','igual')
print(a17)
input('Enter:===')
print(27*'=','\n','Linha de comando finalizada.','\n',27*'=')
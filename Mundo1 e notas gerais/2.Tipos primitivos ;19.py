a8 = str(input('Será que... '))
a9 = str(input('Isso vai ser somado? '))
c3 = a8 + a9
print(f'De certa forma... Sim, e daria a string: {c3}')

a7 = bool(input('?'))
print(f'Se vc digitou algo, o resultado é: {a7}')

a4 = float(input('Primeiro número: '))
a5 = float(input('Menos: '))
a6 = float(input('Dividido por: '))
c2 = ((a4-a5)/a6)
print(f'{a4} menos {a5}, dividido por {a6}. É igual a: {c2}')

a1 = int(input('Primeiro número: '))
a2 = int(input('Mais: '))
a3 = int(input('Vezes: '))
c1 = ((a1+a2)*a3)
print(c1)
print('===')
print('Chegando até aqui, você viu na prática "str, bool, float e int".')

#int(inteiros) = -3, 1, 2, 2187
#float(decimais) = 3.0, 0.013, -1.3927
#bool(verdadeiro ou falso).
#str(string) = 'Olá', '7.5', ''
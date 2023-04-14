from time import sleep


def coinFormat(a1,coin='R$'):
 return f'{coin}{a1:.2f}'.replace('.',',')


def aumentar(a1=float(0),valorizacao=float(0),coin=False):
 a1 = a1+(a1 * valorizacao / 100)
 return f'{a1:.2f}' if coin == False else coinFormat(a1)


def diminuir(a1=float(0),desvalorizacao=float(0),coin=False):
 a1 = a1-(a1 * desvalorizacao / 100)
 return f'{a1:.2f}' if coin == False else coinFormat(a1)


def dobro(a1=float(0),coin=False):
 a1 = a1 * 2
 return a1 if coin == False else coinFormat(a1)


def triplo(a1=float(0),coin=False):
 a1 = a1 * 3
 return a1 if coin == False else coinFormat(a1)


def metade(a1=float(0),coin=False):
 a1 = a1/2
 return f'{a1:.2f}' if coin == False else coinFormat(a1)


def coinResume(a1=0,percentual1=0,percentual0=0):
 print(f'Resumo dos valores:')
 sleep(0.27)
 print('\33[31m===\33[m'*9)
 sleep(0.27)
 print(f'Aumento (+{percentual1}%):   \t\t{aumentar(a1, valorizacao=percentual1, coin=True)}')
 print(f'Diminuição (-{percentual0}%):\t\t{diminuir(a1, desvalorizacao=percentual0, coin=True)}')
 print(f'Dobro:   \t\t\t\t{dobro(a1, coin=True)}')
 print(f'Triplo:  \t\t\t\t{triplo(a1, coin=True)}')
 print(f'Metade:  \t\t\t\t{metade(a1, coin=True)}')


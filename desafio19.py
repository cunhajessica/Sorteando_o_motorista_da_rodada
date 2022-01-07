from random import choice
n1 = str(input('Pessoa 1:'))
n2 = str(input('Pessoa 2:'))
n3 = str(input('Pessoa 3:'))
n4 = str(input('Pessoa 4:'))
lista = (n1, n2, n3, n4)
escolhido = choice(lista)
print('A pessoa escolhida para ser o motorista da rodada foi {}.'.format(escolhido))

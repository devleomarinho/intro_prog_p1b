# Ler uma matriz D 5 x 5 (considere que não serão informados valores duplicados).
# A seguir, leia um número X e escreva uma mensagem indicando se o valor de X
# existe ou NÃO na matriz.

from random import randint

d = []
lista_a = []

while len(lista_a) < 5:
    n = randint(0, 20)
    if n not in lista_a:
        lista_a.append(n)

d.append(lista_a)

lista_b = []

while len(lista_b) < 5:
    n = randint(0, 20)
    if n not in lista_b:
        lista_b.append(n)

d.append(lista_b)

lista_c = []

while len(lista_c) < 5:
    n = randint(0, 20)
    if n not in lista_c:
        lista_c.append(n)

d.append(lista_c)

lista_d = []

while len(lista_d) < 5:
    n = randint(0, 20)
    if n not in lista_d:
        lista_d.append(n)

d.append(lista_d)

lista_e = []

while len(lista_e) < 5:
    n = randint(0, 20)
    if n not in lista_e:
        lista_e.append(n)

d.append(lista_e)

x = int(input('Digite um número para consultar na matriz: '))

encontrado = False

for busca in d:
    if x in busca:
        encontrado = True
        break

if encontrado:
    print(f'O número {x} está na matriz abaixo!\n')
    print(f'{d[0]}\n{d[1]}\n{d[2]}\n{d[3]}\n{d[4]}')
else:
    print(f'O número {x} não está na lista abaixo: ')
    print(f'{d[0]}\n{d[1]}\n{d[2]}\n{d[3]}\n{d[4]}')
from random import randint

v = []

while len(v) < 20:
    n = randint(0, 20)
    if n not in v:
        v.append(n)

num = int(input('Digite um número para consultar na lista: '))

if num in v:
    v.remove(num)
    print(f'Lista atualizada com {num} removido: {v}')
else:
    print(f'O número {num} não consta na lista')

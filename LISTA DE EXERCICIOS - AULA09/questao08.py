from random import randint

v = []

for i in range(30):
    n = randint(0,30)
    v.append(n)

num = int(input('Digite um número: '))

count = 0

for x in v:
    if x == num:
        count +=1

print(f'Lista de números: {v}')
print(f'O número {num} aparece {count} vezes na lista')
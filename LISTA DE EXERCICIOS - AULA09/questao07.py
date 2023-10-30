from random import randint

v1 = []

for n in range(10):
    num = randint(0,10)
    v1.append(num)

v2 = []

for x in range(10):
    number = randint(0,10)
    v2.append(number)

count = 0

for i in range(10):
    if v1[i] == v2[i]:
        count += 1

print(f'Lista v1 = {v1}')
print(f'Lista v2 = {v2}')
print(f'Quantidade de correspondências nas listas = {count}')

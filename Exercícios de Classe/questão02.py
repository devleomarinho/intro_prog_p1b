from random import randint

lista = []
sum = 0

for n in range(10):
    lista.append(randint(1,30))

for i in lista:
    if (i % 2) == 0:
        sum += i

print(f'A lista dos números é {lista}')
print(f'O resultado da soma dos números pares da lista é {sum}')
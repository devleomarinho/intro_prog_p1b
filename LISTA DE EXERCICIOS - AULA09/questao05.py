from random import randint

A = []
B = []

for n in range(10):
    num = randint(0,20)
    A.append(num)

for x in range(10):
    item = randint(0,20)
    B.append(item)

N = []

for i in range(10):
    soma = A[i] + B[i]
    N.append(soma)

print(f'Lista A = {A}')
print(f'Lista B = {B}')
print(f'Lista da soma de A e B = {N}')
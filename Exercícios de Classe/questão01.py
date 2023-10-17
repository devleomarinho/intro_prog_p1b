from random import randint

q = []
for i in range(20):
    q.append(randint(1,100))

maior = -1
menor = 101

for i in q:
    if maior < i:
        maior = i

    if menor > i:
        menor = i

print('Vetor Q =', q)
print(f'O maior número da lista é {maior} e sua posição na lista é {q.index(maior)}')
print(f'O menor número da lista é {menor} e sua posição na lista é {q.index(menor)}')

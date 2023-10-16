from random import randint

q = []
for i in range(20):
    q.append(randint(1,100))

print('Vetor Q =', q)
print('O valor do maior número no vetor Q é =', max(q), 'e sua posição na lista é =', q.index(max(q)))
print('O valor do menor número no vetor Q é =', min(q), 'e sua posição na lista é =', q.index(min(q)))

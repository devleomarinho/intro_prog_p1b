from random import randint

a = []

for i in range(10):
    num = randint(1,30)
    a.append(num)

print(f'A lista inicial de números é: {a}')

x = int(input('Digite o número que ira multiplicar os números da lista: '))

m = []
for item in a:
    multi = item * x
    m.append(multi)

print(f'A lista de números multiplicados por {x} é: {m}')
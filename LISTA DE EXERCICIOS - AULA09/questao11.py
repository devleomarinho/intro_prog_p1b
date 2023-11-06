import random

#Criação da matriz 10x10

matriz = []

while len(matriz) < 100:
    num_aleatorio = random.randint(0,100)
    if num_aleatorio not in matriz:
        matriz.append(num_aleatorio)

nova_matriz = []

for i in range(0, len(matriz),10):
    new = matriz[i:i+10]
    nova_matriz.append(new)

for line in nova_matriz:
    print(line)

maior = nova_matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(10):
    for j in range(10):
        if nova_matriz[i][j] > maior:
            maior = nova_matriz[i][j]
            linha_maior = i
            coluna_maior = j

print('_'*20)
print(f'O maior elemento da matriz é {maior} e está localizado na linha {linha_maior} e coluna {coluna_maior}')
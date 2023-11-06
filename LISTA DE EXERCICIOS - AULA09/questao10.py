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

#Soma de todos os valores da matriz:

sum = 0

for linha in nova_matriz:
    for num in linha:
        sum += num

print(f'\nA soma de todos valores da matriz é: {sum}')

#Soma dos valores da diagona principal:

sum_diag_principal = 0

for i in range(10):
    sum_diag_principal += nova_matriz[i][i]

print(f'A soma dos valores da diagonal principal é: {sum_diag_principal}')

#Soma dos valores da diagonal secundária:

sum_diag_sec = 0

for i in range(10):
    sum_diag_sec += nova_matriz[i][9 - i]

print(f'A soma dos valores da diagonal secundária é: {sum_diag_sec}')

#Soma dos valores da coluna central:

sum_col_central = 0

for i in range(10):
    sum_col_central += nova_matriz[i][4]

print(f'A soma dos valores da coluna central é: {sum_col_central}')
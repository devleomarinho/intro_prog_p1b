from random import randint

notas_turma = []

for item in range(20):
    nota_aluno = randint(1,10)
    notas_turma.append(nota_aluno)

media_turma = sum(notas_turma) / 20

aprovados = []

for nota in notas_turma:
    if nota >= media_turma:
        aprovados.append(nota)


print(f'As notas desta turma são: {notas_turma}')
print(f'A média desta turma é: {media_turma}')
print(f'As notas acima da média são: {aprovados}')
print(f'O total de alunos aprovados foi: {len(aprovados)}')
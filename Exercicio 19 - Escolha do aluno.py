import random

lista_alunos = []
alu1 = lista_alunos.append(str(input('1° aluno: ')))
alu2 = lista_alunos.append(str(input('2° aluno: ')))
alu3 = lista_alunos.append(str(input('3° aluno: ')))
alu4 = lista_alunos.append(str(input('4° aluno: ')))
escolha = random.choice(lista_alunos)
print(escolha)
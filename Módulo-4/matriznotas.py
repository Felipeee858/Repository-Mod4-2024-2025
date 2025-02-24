"""Um programa para ler as notas de 10 alunos em 5 disciplinas e calcular:
-a média de cada aluno
-a média de cada disciplina
Hacker:
-mostrar o nº do aluno com melhor média
-mostrar quantos alunos não têm negativa (sem nota<10)"""

import numpy as np
TAMANHO=(1,5)
notas=np.zeros(TAMANHO,dtype="i")

def LerDados(notas):
    """Função para percorrer as linhas e colunas da matriz notas e preencher com os dados
    inseridos pelo utilizador"""
    #ler as notas por aluno(linhas)
for l in range(notas.shape[0]):
    for c in range(notas.shape[1]):
        notas[l,c]=float(input("Introduza a nota: "))
def MediaPorAluno(notas):
    """Função para percorrer a matriz e calcular a média para cada um dos 10 alunos"""
    for l in range(notas.shape[0]):
        soma=0
        for c in range(notas.shape[1]):
            soma=soma+notas[l,c]
        print(soma/5)
def MediaPorDisciplinas(notas):
    """Função para percorrer a matriz e calcular a média para cada uma das 5 disciplinas"""
    for c in range(notas.shape[1]):
        soma=0
        for l in range(notas.shape[0]):
            soma=soma+notas[l,c]
        print(soma/5)

LerDados(notas)
MediaPorAluno(notas)
MediaPorDisciplinas(notas)
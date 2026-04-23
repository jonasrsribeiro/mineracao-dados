import pandas as pd
import numpy as np

dados_cursos = {
    'id_curso': [1, 2, 3, 4],
    'nome_curso': ['Engenharia de Software', 'Ciência da Computação', 'Sistemas de Informação', 'Redes de Computadores']
}
df_cursos = pd.DataFrame(dados_cursos)

dados_disciplinas = {
    'id_disciplina': [10, 11, 12, 13, 14, 15, 16, 17, 18],
    'nome_disciplina': ['Algoritmos', 'Banco de Dados', 'Redes', 'Engenharia de Requisitos',
                        'Programação Web', 'Sistemas Operacionais', 'Inteligência Artificial', 'Segurança da Informação',
                        'Cálculo Numérico'],
    'id_curso': [1, 1, 2, 1, 2, 3, 2, 4, 3]
}
df_disciplinas = pd.DataFrame(dados_disciplinas)

dados_professores = {
    'id_professor': [100, 101, 102, 103, 104],
    'nome_professor': ['Prof. Antônio', 'Prof. Beatriz', 'Prof. César', 'Prof. Daniela', 'Prof. Eduardo'],
    'titulacao': ['Doutor', 'Mestre', 'Doutor', 'Mestre', 'Doutor']
}
df_professores = pd.DataFrame(dados_professores)

dados_alunos = {
    'id_aluno': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012],
    'nome_aluno': ['Alice', 'Bernardo', 'Carla', 'Diego', 'Elisa', 'Fábio',
                   'Giovana', 'Henrique', 'Iris', 'João', 'Karen', 'Lucas'],
    'semestre': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],
    'id_curso': [1, 1, 2, 2, 3, 3, 4, 4, 1, 2, 3, 4]
}
df_alunos = pd.DataFrame(dados_alunos)

dados_matriculas = {
    'id_matricula':  [1,    2,    3,    4,    5,    6,    7,    8,    9,   10,   11,   12,   13,   14,   15,   16,   17,   18,   19,   20],
    'id_aluno':      [1001, 1001, 1002, 1002, 1003, 1003, 1004, 1005, 1005, 1006, 1007, 1008, 1008, 1009, 1010, 1010, 1011, 1011, 1012, 1012],
    'id_disciplina': [10,   11,   10,   14,   12,   16,   13,   15,   10,   11,   17,   12,   18,   10,   16,   15,   11,   13,   17,   18],
    'id_professor':  [100,  101,  100,  102,  103,  104,  102,  101,  100,  103,  104,  103,  104,  100,  101,  102,  103,  102,  104,  104],
    'nota':          [8.5,  7.0,  9.0,  6.5,  7.5,  8.0,  9.5,  6.0,  7.0,  8.5,  9.0,  5.5,  7.5,  8.0,  6.5,  9.0,  7.0,  8.0,  9.5,  6.0]
}
df_matriculas = pd.DataFrame(dados_matriculas)

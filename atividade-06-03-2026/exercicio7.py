import pandas as pd

dados = {
    'ID_Paciente': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Elisa', 'Fábio', 'Giovana', 'Henrique', 'Iris', 'João'],
    'Altura_Metros': [1.65, 1.80, 165.0, 1.72, 0.30, 1.58, 1.90, 18.0, 1.75, 1.68]
}

df = pd.DataFrame(dados)

ALTURA_MIN = 0.5
ALTURA_MAX = 2.5

impossiveis = df[(df['Altura_Metros'] < ALTURA_MIN) | (df['Altura_Metros'] > ALTURA_MAX)]

print("Dados originais:")
print(df)
print(f"\nPacientes com alturas fisicamente impossíveis (fora de {ALTURA_MIN}m a {ALTURA_MAX}m):")
print(impossiveis)

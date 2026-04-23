import pandas as pd

ANO_ATUAL = 2026

dados = {
    'ID_Aluno': [1, 2, 3, 4, 5, 6, 7, 8],
    'Nome': ['Alice', 'Bruno', 'Carla', 'Diego', 'Elisa', 'Fábio', 'Giovana', 'Henrique'],
    'Ano_Nascimento': [2005, 2004, 2003, 2006, 2004, 2000, 2005, 2003],
    'Idade_Declarada': [21, 22, 23, 20, 21, 26, 20, 23]
}

df = pd.DataFrame(dados)

df['Idade_Real'] = ANO_ATUAL - df['Ano_Nascimento']

inconsistentes = df[df['Idade_Real'] != df['Idade_Declarada']]

print("Dados com idades calculadas:")
print(df)
print("\nRegistros com contradição entre idade real e declarada:")
print(inconsistentes)

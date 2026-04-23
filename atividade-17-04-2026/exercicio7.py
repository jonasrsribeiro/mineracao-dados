import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Paciente':        ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Carla'],
    'Pressao_Sistolica': [120.0, np.nan, 135.0, np.nan, 118.0, np.nan],
    'Glicemia':          [95.0, 110.0, np.nan, np.nan, 88.0, 102.0]
})

print("Dados com valores ausentes:")
print(df, "\n")

df['Flag_Omissao_Pressao'] = df['Pressao_Sistolica'].isnull().astype(int)
df['Flag_Omissao_Glicemia'] = df['Glicemia'].isnull().astype(int)

df['Pressao_Sistolica'] = df['Pressao_Sistolica'].fillna(df['Pressao_Sistolica'].mean())
df['Glicemia'] = df['Glicemia'].fillna(df['Glicemia'].mean())

print("Após criar indicadores de omissão e preencher lacunas:")
print(df)

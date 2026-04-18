import pandas as pd
import numpy as np

dados = {'temperatura': [80, 82, 85, 81, 300, 83]}
df = pd.DataFrame(dados)

print("DataFrame original:")
print(df)

mediana = df['temperatura'].median()

q1 = df['temperatura'].quantile(0.25)
q3 = df['temperatura'].quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"\nMediana (Q2) = {mediana}")
print(f"Limite Inferior = {limite_inferior} | Limite Superior = {limite_superior}")

df['temperatura'] = np.where(
    (df['temperatura'] < limite_inferior) | (df['temperatura'] > limite_superior),
    mediana,
    df['temperatura']
)

print("\nDataFrame após substituição do outlier pela mediana:")
print(df)
print(f"\nNúmero de linhas preservado: {len(df)}")

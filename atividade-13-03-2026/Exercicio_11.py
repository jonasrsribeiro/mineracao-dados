import pandas as pd

df = pd.read_csv('dados_sensores.csv')

print("Primeiras linhas do DataFrame:")
print(df.head())
print(f"\nFormato: {df.shape[0]} linhas x {df.shape[1]} colunas")

print("\n--- Leituras ausentes (NaN) por coluna ---")
print(df.isna().sum())

for coluna in ['temperatura_celsius', 'pressao_psi']:
    mediana_col = df[coluna].median()
    df[coluna] = df[coluna].fillna(mediana_col)
    print(f"NaN em '{coluna}' substituídos pela mediana: {mediana_col}")

print("\n--- NaN após substituição ---")
print(df.isna().sum())

print("\nDataFrame após tratamento:")
print(df.head(10))

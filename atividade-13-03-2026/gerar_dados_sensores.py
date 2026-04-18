import pandas as pd
import numpy as np

np.random.seed(42)
n = 50

id_leitura = list(range(1, n + 1))

temperatura = np.random.normal(loc=75, scale=3, size=n).round(2)
pressao = np.random.normal(loc=100, scale=5, size=n).round(2)

temperatura[10] = 250.0
temperatura[30] = 300.0
pressao[20] = 500.0

indices_nan_temp = np.random.choice(n, size=5, replace=False)
indices_nan_pres = np.random.choice(n, size=4, replace=False)

temperatura[indices_nan_temp] = np.nan
pressao[indices_nan_pres] = np.nan

df = pd.DataFrame({
    'id_leitura': id_leitura,
    'temperatura_celsius': temperatura,
    'pressao_psi': pressao
})

df.to_csv('dados_sensores.csv', index=False)
print("Arquivo 'dados_sensores.csv' gerado com sucesso!")
print(df.head(10))
print(f"\nNaN em temperatura: {df['temperatura_celsius'].isna().sum()}")
print(f"NaN em pressao:     {df['pressao_psi'].isna().sum()}")

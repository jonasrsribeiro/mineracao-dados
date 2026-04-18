import pandas as pd
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

producao = [100, 102, 98, 105, 500, 101]

df = pd.DataFrame({'producao': producao})
df['z_score'] = zscore(df['producao'])

df_limpo = df[df['z_score'].abs() <= 2].copy()

print("Dados com Z-Score:")
print(df)
print("\nOutlier removido. Dados limpos:")
print(df_limpo[['producao']])

scaler = MinMaxScaler()
df_limpo['normalizado'] = scaler.fit_transform(df_limpo[['producao']])

print("\nProdução normalizada (0 a 1):")
print(df_limpo[['producao', 'normalizado']])

print("""
Por que normalizar DEPOIS de remover outliers?
- Se o 500 ainda estivesse na lista, ele seria o máximo (max=500).
- Todos os valores normais (98-105) ficariam comprimidos próximos de 0.
- A escala seria dominada pelo outlier e perderia poder de diferenciação.
- Removendo o outlier primeiro, os dados normais ocupam toda a faixa 0-1.
""")

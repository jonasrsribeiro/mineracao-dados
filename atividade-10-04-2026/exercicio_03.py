import pandas as pd
from scipy.stats import zscore

df = pd.DataFrame({'vendas': [1200, 1350, 1250, 1300, 13500, 1280]})

df['z_score'] = zscore(df['vendas'])

dados_limpos = df[(df['z_score'] >= -3) & (df['z_score'] <= 3)]

print("DataFrame original:")
print(df)
print("\nDados limpos (Z-Score entre -3 e 3):")
print(dados_limpos)

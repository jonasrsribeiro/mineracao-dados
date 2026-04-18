import pandas as pd

df = pd.read_csv('dados_sensores.csv')

for coluna in ['temperatura_celsius', 'pressao_psi']:
    df[coluna] = df[coluna].fillna(df[coluna].median())

print(f"Linhas antes da limpeza: {len(df)}")

q1_temp = df['temperatura_celsius'].quantile(0.25)
q3_temp = df['temperatura_celsius'].quantile(0.75)
iqr_temp = q3_temp - q1_temp
li_temp = q1_temp - 1.5 * iqr_temp
ls_temp = q3_temp + 1.5 * iqr_temp

print(f"\nTemperatura -> LI: {li_temp:.2f} | LS: {ls_temp:.2f}")

q1_pres = df['pressao_psi'].quantile(0.25)
q3_pres = df['pressao_psi'].quantile(0.75)
iqr_pres = q3_pres - q1_pres
li_pres = q1_pres - 1.5 * iqr_pres
ls_pres = q3_pres + 1.5 * iqr_pres

print(f"Pressão     -> LI: {li_pres:.2f} | LS: {ls_pres:.2f}")

mascara_temp = (df['temperatura_celsius'] >= li_temp) & (df['temperatura_celsius'] <= ls_temp)
mascara_pres = (df['pressao_psi'] >= li_pres) & (df['pressao_psi'] <= ls_pres)

df_limpo = df[mascara_temp & mascara_pres]

print(f"\nLinhas após remoção de outliers: {len(df_limpo)}")
print(f"Linhas removidas: {len(df) - len(df_limpo)}")

df_limpo.to_csv('dados_validados.csv', index=False, decimal=',')
print("\nArquivo 'dados_validados.csv' exportado com sucesso!")
print(df_limpo.head())

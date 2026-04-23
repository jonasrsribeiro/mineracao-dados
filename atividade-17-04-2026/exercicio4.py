import pandas as pd

df_transacoes = pd.DataFrame({
    'ID_Cliente': [1, 1, 1, 2, 2, 3, 3, 3, 3, 4],
    'Data': pd.to_datetime([
        '2026-01-10', '2026-02-15', '2026-04-10',
        '2025-12-05', '2026-04-01',
        '2026-03-20', '2026-03-28', '2026-04-05', '2026-04-15',
        '2025-11-01'
    ]),
    'Valor': [250.0, 400.0, 180.0, 900.0, 650.0, 120.0, 200.0, 150.0, 300.0, 75.0]
})

data_referencia = pd.to_datetime('2026-04-17')

print("Log de transações bruto:")
print(df_transacoes, "\n")

grupo = df_transacoes.groupby('ID_Cliente')

df_rfm = pd.DataFrame({
    'Frequencia':     grupo['Valor'].count(),
    'Valor_Monetario': grupo['Valor'].sum(),
    'Ultima_Compra':  grupo['Data'].max()
}).reset_index()

df_rfm['Recencia_Dias'] = (data_referencia - df_rfm['Ultima_Compra']).dt.days

print("Perfil RFM por cliente:")
print(df_rfm[['ID_Cliente', 'Recencia_Dias', 'Frequencia', 'Valor_Monetario']])

import pandas as pd

FERIADOS_EVENTOS = {
    '2025-11-28': 'Black Friday',
    '2025-12-25': 'Natal',
    '2026-11-27': 'Black Friday',
    '2026-12-25': 'Natal',
    '2026-04-21': 'Tiradentes',
    '2026-05-01': 'Dia do Trabalho',
}

df = pd.DataFrame({
    'ID_Transacao': [1, 2, 3, 4, 5, 6, 7, 8],
    'Data_Transacao': pd.to_datetime([
        '2025-11-28', '2026-04-15', '2025-12-25', '2026-03-10',
        '2026-04-21', '2026-02-20', '2026-05-01', '2026-06-15'
    ]),
    'Valor': [1200.0, 350.0, 980.0, 150.0, 430.0, 75.0, 510.0, 200.0]
})

print("Dados brutos:")
print(df, "\n")

df['Data_Str'] = df['Data_Transacao'].dt.strftime('%Y-%m-%d')
df['Nome_Evento'] = df['Data_Str'].map(FERIADOS_EVENTOS).fillna('Normal')
df['Flag_Pico_Vendas'] = df['Nome_Evento'].ne('Normal').astype(int)
df = df.drop(columns=['Data_Str'])

print("Após identificação de feriados e eventos:")
print(df)

import pandas as pd

df = pd.DataFrame({
    'Usuario': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena'],
    'Timestamp': [
        '2026-04-13 09:15:00',
        '2026-04-14 22:30:00',
        '2026-04-15 14:00:00',
        '2026-04-16 08:45:00',
        '2026-04-17 11:20:00',
        '2026-04-18 16:00:00',
        '2026-04-19 10:00:00',
        '2026-04-20 21:00:00'
    ]
})

print("Dados brutos:")
print(df, "\n")

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Mes'] = df['Timestamp'].dt.month
df['Dia_Semana'] = df['Timestamp'].dt.day_name()
df['Num_Dia_Semana'] = df['Timestamp'].dt.dayofweek

df['Flag_Final_Semana'] = (df['Num_Dia_Semana'] >= 5).astype(int)

print("Após decomposição de datas:")
print(df[['Usuario', 'Timestamp', 'Mes', 'Dia_Semana', 'Flag_Final_Semana']])

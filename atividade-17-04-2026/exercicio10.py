import pandas as pd

df = pd.DataFrame({
    'Sensor_ID': ['TMP-01', 'TMP-02', 'TMP-03', 'TMP-04', 'TMP-05'],
    'Leitura_1': [10.0, 20.0, 15.0, 30.0, 5.0],
    'Leitura_2': [12.0, 22.0, 20.0, 40.0, 6.0],
    'Leitura_3': [15.0, 24.0, 30.0, 60.0, 7.0]
})

print("Leituras brutas:")
print(df, "\n")

df['Delta_1'] = df['Leitura_2'] - df['Leitura_1']
df['Delta_2'] = df['Leitura_3'] - df['Leitura_2']

df['Aceleracao'] = df['Delta_2'] - df['Delta_1']

df['Flag_Alerta_Exponencial'] = (df['Aceleracao'] > df['Delta_1']).astype(int)

print("Após calcular delta do delta (aceleração):")
print(df)

import pandas as pd

df = pd.DataFrame({
    'Sensor_ID': ['TMP-01', 'TMP-02', 'TMP-03', 'TMP-04', 'TMP-05'],
    'Leitura_Momento_1': [22.5, 45.0, 18.3, 60.0, 31.2],
    'Leitura_Momento_2': [25.1, 41.5, 27.8, 58.0, 29.0]
})

print("Leituras brutas:")
print(df, "\n")

df['Delta'] = df['Leitura_Momento_2'] - df['Leitura_Momento_1']

df['Evolucao_Percentual'] = (df['Delta'] / df['Leitura_Momento_1']) * 100

df['Tendencia'] = df['Delta'].apply(lambda x: 'Crescimento' if x > 0 else 'Queda')

print("Após cálculo de deltas e tendência:")
print(df)

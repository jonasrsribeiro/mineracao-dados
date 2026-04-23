import pandas as pd

df = pd.DataFrame({
    'Produto':        ['ESP32', 'Raspberry Pi 4', 'Arduino Uno', 'Orange Pi', 'SSD 480GB', 'Memória RAM', 'Webcam HD'],
    'Volume_Vendas':  [1500, 320, 980, 210, 750, 1100, 430]
})

print("Volumes brutos (sem contexto de grupo):")
print(df, "\n")

df['Ranking_Interno'] = df['Volume_Vendas'].rank(ascending=False).astype(int)

df = df.sort_values(by='Ranking_Interno')

print("Após aplicar ranking interno:")
print(df)

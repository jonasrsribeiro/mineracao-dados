import pandas as pd
import numpy as np

dados = {
    'Sensor_ID': ['ESP32-01', 'ESP32-01', 'ESP32-01', 'ESP32-02', 'ESP32-02',
                  'ESP32-02', 'ESP32-03', 'ESP32-03', 'ESP32-03', 'ESP32-03'],
    'Temperatura_C': ['23.5', '24.1', 'falha_sinal', '21.8', 'falha_sinal',
                      '22.3', '25.0', 'falha_sinal', '24.7', 'falha_sinal']
}

df = pd.DataFrame(dados)

df['Temperatura_C'] = pd.to_numeric(df['Temperatura_C'], errors='coerce')

falhas = df[df['Temperatura_C'].isnull()]

print("Dados originais:")
print(df)
print("\nLinhas com falha de conversão:")
print(falhas)

import pandas as pd
import numpy as np

dados = {
    'Sensor_ID': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
    'Valor_Leitura': [10, 12, 11, 13, 100, 200, 205, 198, 202, 5]
}

df = pd.DataFrame(dados)
print("DataFrame original:")
print(df)

anomalias_por_grupo = []

for sensor, grupo in df.groupby('Sensor_ID'):
    q1 = grupo['Valor_Leitura'].quantile(0.25)
    q3 = grupo['Valor_Leitura'].quantile(0.75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    print(f"\nSensor {sensor}: Q1={q1} | Q3={q3} | IQR={iqr}")
    print(f"  Limite Inferior={limite_inferior} | Limite Superior={limite_superior}")

    mascara_anomalia = (grupo['Valor_Leitura'] < limite_inferior) | \
                       (grupo['Valor_Leitura'] > limite_superior)
    anomalias = grupo[mascara_anomalia]

    if not anomalias.empty:
        print(f"  Anomalias encontradas no Sensor {sensor}:")
        print(anomalias)
        anomalias_por_grupo.append(anomalias)
    else:
        print(f"  Nenhuma anomalia no Sensor {sensor}.")

if anomalias_por_grupo:
    df_anomalias = pd.concat(anomalias_por_grupo)
    print("\nResumo de todas as anomalias:")
    print(df_anomalias)

import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.DataFrame({
    'Idade': [22, 25, 21, 23, 24, 150],
    'Horas_Estudo': [10, 8, 12, 9, 11, 7],
    'Nota_Final': [7.5, 8.0, 9.0, 7.0, 8.5, 6.0]
})

floresta = IsolationForest(random_state=42)

df['Outlier'] = floresta.fit_predict(df[['Idade', 'Horas_Estudo', 'Nota_Final']])

print("DataFrame completo:")
print(df)

print("\nLinha(s) detectada(s) como anomalia:")
print(df[df['Outlier'] == -1])

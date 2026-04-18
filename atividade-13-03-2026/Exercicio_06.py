import numpy as np

def detectar_anomalias(dados, multiplicador):
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1

    limite_inferior = q1 - multiplicador * iqr
    limite_superior = q3 + multiplicador * iqr

    print(f"Q1 = {q1} | Q3 = {q3} | IQR = {iqr}")
    print(f"Limite Inferior = {limite_inferior} | Limite Superior = {limite_superior}")

    outliers = [v for v in dados if v < limite_inferior or v > limite_superior]
    return outliers


vetor = [45, 50, 55, 60, 48, 52, 51, 98, 49, 53]

print(f"Vetor: {vetor}")
resultado = detectar_anomalias(vetor, 1.5)
print(f"\nOutliers encontrados: {resultado}")

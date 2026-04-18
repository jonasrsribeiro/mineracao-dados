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

if __name__ == "__main__":
    dados_teste = [20, 25, 30, 35, 40, 45, 90]
    resultado = detectar_anomalias(dados_teste, 1.5)
    print(f"Outliers encontrados: {resultado}")

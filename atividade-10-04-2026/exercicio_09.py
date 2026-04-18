import pandas as pd
from sklearn.preprocessing import MinMaxScaler

valor_manual = (200 - 100) / (500 - 100)
print(f"Valor normalizado manual de 200 psi: {valor_manual}")

pressao = [[100], [200], [500]]

scaler = MinMaxScaler()

resultado = scaler.fit_transform(pressao)

print(f"\nResultado do MinMaxScaler:")
for original, normalizado in zip(pressao, resultado):
    print(f"{original[0]} psi -> {normalizado[0]:.4f}")

print(f"\nValor de 200 psi pelo scaler: {resultado[1][0]:.4f} (bate com o manual: {valor_manual:.4f})")

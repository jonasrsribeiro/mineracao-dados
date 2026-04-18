import pandas as pd
from sklearn.preprocessing import MinMaxScaler

temps = [[-20], [-10], [0], [20]]

scaler = MinMaxScaler()

resultado = scaler.fit_transform(temps)

print("Temperatura original -> Normalizada:")
for original, normalizado in zip(temps, resultado):
    print(f"{original[0]}°C -> {normalizado[0]:.4f}")

print("""
Explicação:
- O 0°C original NÃO continua sendo 0.0 após a normalização.
- O MinMaxScaler usa a fórmula (x - min) / (max - min).
- O mínimo é -20, então: (0 - (-20)) / (20 - (-20)) = 20/40 = 0.5
- O novo valor 0.0 representa o menor valor da lista (-20°C), não o zero absoluto.
- O zero da escala normalizada é relativo ao conjunto de dados, não ao zero real.
""")

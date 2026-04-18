import numpy as np

tempos = [20, 25, 30, 35, 40, 45, 90]

q1 = np.percentile(tempos, 25)
q2 = np.percentile(tempos, 50)
q3 = np.percentile(tempos, 75)

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")

outliers = [v for v in tempos if v < limite_inferior or v > limite_superior]
print(f"\nOutliers detectados: {outliers}")

# Comparação com Exemplo_01 (biblioteca statistics):
# Exemplo_01 usa statistics.median() com fatiamento manual [:3] e [4:]
#   Q1 = 25.0  |  Q2 = 35.0  |  Q3 = 45.0  (método Tukey/exclusivo)
#
# Exemplo_03 usa np.percentile() com interpolação linear (método padrão)
#   Q1 = 28.75 |  Q2 = 35.0  |  Q3 = 43.75 (interpolação linear)
#
# A diferença ocorre porque o NumPy por padrão usa interpolação linear
# entre os valores adjacentes, enquanto o statistics.median() com fatiamento
# manual aplica o método de Tukey (mediana das metades excluindo a mediana central).
# O resultado do IQR e dos limites, portanto, também difere entre os dois métodos.

import numpy as np

tensoes = [110, 115, 120, 118, 112, 220, 116, 114, 119, 12]

q1 = np.percentile(tensoes, 25)
q3 = np.percentile(tensoes, 75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"Vetor de tensões: {tensoes}")
print(f"Q1 = {q1} | Q3 = {q3} | IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")

anomalias = [v for v in tensoes if v < limite_inferior or v > limite_superior]

print(f"\nValores anômalos detectados: {anomalias}")

import numpy as np

tempos = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]

p25 = np.percentile(tempos, 25)
p50 = np.percentile(tempos, 50)
p75 = np.percentile(tempos, 75)

iqr = p75 - p25

limite_inferior = p25 - 1.5 * iqr
limite_superior = p75 + 1.5 * iqr

print(f"Vetor: {tempos}")
print(f"Q1 (P25) = {p25}")
print(f"Q2 (P50) = {p50}")
print(f"Q3 (P75) = {p75}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")

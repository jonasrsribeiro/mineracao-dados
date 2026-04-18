import numpy as np

tempos = [12, 15, 14, 13, 16, 12, 14, 150, 13, 15]

p25 = np.percentile(tempos, 25)
p50 = np.percentile(tempos, 50)
p75 = np.percentile(tempos, 75)

print(f"Vetor: {tempos}")
print(f"Percentil 25 (Q1) = {p25}")
print(f"Percentil 50 (Q2) = {p50}")
print(f"Percentil 75 (Q3) = {p75}")

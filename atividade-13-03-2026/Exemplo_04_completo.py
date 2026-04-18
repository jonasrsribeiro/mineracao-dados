import numpy as np

tempos = [20, 25, 30, 35, 40, 45, 90]

q1, q2, q3 = np.percentile(tempos, [25, 50, 75])

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

# Exemplo_04 é funcionalmente idêntico ao Exemplo_03:
# a única diferença é que np.percentile() recebe uma lista [25, 50, 75]
# e retorna os três quartis em uma única chamada (desempacotados diretamente).
#
# Comparação com Exemplo_01 (statistics):
#   Exemplo_01  -> Q1=25.0,  Q2=35.0, Q3=45.0  (Tukey / fatiamento manual)
#   Exemplo_03/04 -> Q1=28.75, Q2=35.0, Q3=43.75 (interpolação linear NumPy)
#
# Ambos os exemplos 03 e 04 produzem resultados idênticos entre si.

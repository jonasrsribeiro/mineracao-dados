import statistics

tempos = [20, 25, 30, 35, 40, 45, 90]

tempos_sorted = sorted(tempos)
n = len(tempos_sorted)

q2 = statistics.median(tempos_sorted)

meio = n // 2
if n % 2 == 0:
    inferior = tempos_sorted[:meio]
    superior = tempos_sorted[meio:]
else:
    inferior = tempos_sorted[:meio]
    superior = tempos_sorted[meio + 1:]

q1 = statistics.median(inferior)
q3 = statistics.median(superior)

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"N = {n} elementos")
print(f"Inferior = {inferior}")
print(f"Superior = {superior}")
print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")

print("\n--- Verificação de Outliers (limites baseados no IQR) ---")
outliers = [v for v in tempos_sorted if v < limite_inferior or v > limite_superior]

if outliers:
    print(f"Outliers encontrados: {outliers}")
else:
    print("Nenhum outlier encontrado no conjunto.")

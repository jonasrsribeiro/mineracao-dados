import statistics

tempos = [20, 25, 30, 35, 40, 45, 90]

q2 = statistics.median(tempos)

inferior = tempos[:3]
superior = tempos[4:]

q1 = statistics.median(inferior)
q3 = statistics.median(superior)

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

print(f"Inferior = {inferior}")
print(f"Superior = {superior}")
print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")
print(f"IQR = {iqr}")
print(f"Limite Inferior = {limite_inferior}")
print(f"Limite Superior = {limite_superior}")

print("\n--- Verificação de Outliers (limites fixos: < -5 ou > 75) ---")
outliers_encontrados = False
for valor in tempos:
    if valor < -5 or valor > 75:
        print(f"Outlier encontrado: {valor}")
        outliers_encontrados = True

if not outliers_encontrados:
    print("Nenhum outlier encontrado no conjunto.")

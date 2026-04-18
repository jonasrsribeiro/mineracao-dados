import statistics

dados = [100, 150, 200, 250, 300, 350]

n = len(dados)
meio = n // 2

if n % 2 == 0:
    metade_inferior = dados[:meio]
    metade_superior = dados[meio:]
else:
    metade_inferior = dados[:meio]
    metade_superior = dados[meio + 1:]

q1 = statistics.median(metade_inferior)
q2 = statistics.median(dados)
q3 = statistics.median(metade_superior)

print(f"Dados: {dados}")
print(f"N = {n} elementos (par)")
print(f"Metade inferior: {metade_inferior}")
print(f"Metade superior: {metade_superior}")
print(f"Q1 = {q1}")
print(f"Q2 = {q2}")
print(f"Q3 = {q3}")

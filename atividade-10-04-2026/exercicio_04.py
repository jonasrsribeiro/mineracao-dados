from scipy.stats import zscore
import numpy as np

medidas = [10, 12, 11, 10, 10000]

z_scores = zscore(medidas)

media = np.mean(medidas)
desvio = np.std(medidas)

print(f"Média: {media:.2f}")
print(f"Desvio Padrão: {desvio:.2f}")
print(f"Z-Score do valor 10000: {z_scores[-1]:.4f}")

if z_scores[-1] > 3:
    print("O valor 10000 ultrapassa a marca de 3 sigmas.")
else:
    print("O valor 10000 NÃO ultrapassa a marca de 3 sigmas.")
    print("O desvio padrão explodiu por causa do outlier colossal, mascarando a anomalia.")

from scipy.stats import zscore

temp = [45.5, 46.0, 45.2, 45.8, 46.1, 98.0, 45.9, 45.3]

z_scores = zscore(temp)

for i, z in enumerate(z_scores):
    if z > 2.5:
        print(f"Anomalia detectada: {temp[i]} (Z-Score: {z:.2f})")

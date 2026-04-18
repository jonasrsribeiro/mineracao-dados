from sklearn.ensemble import IsolationForest
import numpy as np

np.random.seed(42)

normais = np.random.normal(loc=0, scale=1, size=(1000, 2))
absurdos = np.random.uniform(low=100, high=200, size=(50, 2))
dados = np.vstack([normais, absurdos])

floresta_05 = IsolationForest(contamination=0.05, random_state=42)
pred_05 = floresta_05.fit_predict(dados)
anomalias_05 = (pred_05 == -1).sum()

floresta_20 = IsolationForest(contamination=0.20, random_state=42)
pred_20 = floresta_20.fit_predict(dados)
anomalias_20 = (pred_20 == -1).sum()

print(f"Anomalias com contamination=0.05: {anomalias_05}")
print(f"Anomalias com contamination=0.20: {anomalias_20}")
print("\nQuanto maior o contamination, mais pontos são marcados como anomalia.")

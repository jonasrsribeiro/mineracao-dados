from sklearn.ensemble import IsolationForest

servidores = [[20, 30], [25, 35], [22, 32], [99, 95], [21, 31]]

floresta = IsolationForest(random_state=42)

floresta.fit(servidores)

predicoes = floresta.predict(servidores)

print("Predições:", predicoes)
print("\nLegenda: +1 = normal | -1 = anomalia")
for i, pred in enumerate(predicoes):
    status = "ANOMALIA" if pred == -1 else "Normal"
    print(f"Servidor {i} {servidores[i]}: {status}")

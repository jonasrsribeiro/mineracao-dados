from sklearn.ensemble import IsolationForest

alunos = [[8, 2], [7, 4], [9, 1], [8, 3], [2, 25], [9, 25]]

floresta = IsolationForest(random_state=42)

predicoes = floresta.fit_predict(alunos)

print("Resultado da análise multivariada (Nota + Faltas):")
for i, pred in enumerate(predicoes):
    status = "ANOMALIA (-1)" if pred == -1 else "Normal (+1)"
    print(f"Aluno {alunos[i]}: {status}")

print("\nO aluno [9, 25] tem nota alta mas faltas altas — combinação rara.")
print("O Z-Score individual de notas não detectaria, mas o Isolation Forest detecta.")

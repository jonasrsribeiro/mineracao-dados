import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({
    'Saldo':  [1_000_000, 1_000_010],
    'Risco':  [0.1, 0.9]
}, index=['Cliente A', 'Cliente B'])

print("Dados originais:")
print(df)

print("""
Explicação sem normalização:
- A diferença de saldo é R$10, num universo de R$1.000.000.
- A IA enxerga distâncias numéricas: 10 vs 0.8 (diferença de risco).
- O saldo domina totalmente o cálculo de distância e a variação de risco (0.8)
  some perto de 10 reais — a IA conclui que os clientes são quase idênticos.
""")

scaler = MinMaxScaler()

df_norm = pd.DataFrame(
    scaler.fit_transform(df),
    columns=df.columns,
    index=df.index
)

print("Dados normalizados:")
print(df_norm)
print("\nApós normalizar: diferença de saldo = 1.0 vs diferença de risco = 1.0")
print("Os R$10 de saldo viram diferença mínima, e o risco ganha o peso correto.")

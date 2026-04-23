import pandas as pd

df = pd.DataFrame({
    'Cliente':       ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Renda_Mensal':  [5000.0, 3200.0, 8500.0, 1800.0, 12000.0],
    'Divida_Total':  [1500.0, 2800.0, 1700.0, 1600.0, 3000.0]
})

print("Atributos isolados:")
print(df, "\n")

df['Razao_Comprometimento'] = df['Divida_Total'] / df['Renda_Mensal']

df['Risco_Credito'] = df['Razao_Comprometimento'].apply(
    lambda x: 'Alto' if x > 0.40 else ('Moderado' if x > 0.20 else 'Baixo')
)

print("Após interação entre atributos:")
print(df)
print("\nA razão combina renda e dívida em uma única feature relacional,")
print("permitindo à IA comparar clientes de rendas diferentes de forma justa.")

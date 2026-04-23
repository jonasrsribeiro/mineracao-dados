import pandas as pd

dados = {
    'ID_Compra': [1, 2, 3, 4, 5, 6, 7, 8],
    'Produto': ['Teclado', 'Monitor', 'Mouse', 'SSD', 'Webcam', 'Headset', 'Placa ESP32', 'Raspberry Pi'],
    'Data_Compra':   pd.to_datetime(['2026-01-05', '2026-01-10', '2026-01-15', '2026-01-20',
                                     '2026-01-22', '2026-01-25', '2026-02-01', '2026-02-05']),
    'Data_Entrega':  pd.to_datetime(['2026-01-10', '2026-01-08', '2026-01-20', '2026-01-25',
                                     '2026-01-19', '2026-01-30', '2026-01-28', '2026-02-10'])
}

df = pd.DataFrame(dados)

inconsistentes = df[df['Data_Entrega'] < df['Data_Compra']]

print("Dados originais:")
print(df)
print("\nCompras com entrega antes do pedido:")
print(inconsistentes)

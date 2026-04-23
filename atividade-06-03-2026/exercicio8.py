import pandas as pd

CAPACIDADE_MAXIMA = 10000

dados = {
    'ID_Componente': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Componente': ['Resistor 10k', 'Capacitor 100uF', 'LED Vermelho', 'Transistor BC547',
                   'Placa ESP32', 'Cabo USB', 'Botão Táctil', 'Display OLED', 'Sensor DHT22', 'Relé 5V'],
    'Quantidade_Estoque': [500, -20, 1200, 0, -5, 15200, 300, -1, 450, 99.7]
}

df = pd.DataFrame(dados)

invalidos = df[(df['Quantidade_Estoque'] < 0) |
               (df['Quantidade_Estoque'] > CAPACIDADE_MAXIMA) |
               (df['Quantidade_Estoque'] != df['Quantidade_Estoque'].astype(int))]

print("Dados originais:")
print(df)
print(f"\nComponentes com falha de integridade (negativo, acima de {CAPACIDADE_MAXIMA} ou fracionado):")
print(invalidos)

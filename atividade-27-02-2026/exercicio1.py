import pandas as pd
import numpy as np

dados_clientes = {
    'id_cliente': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nome_cliente': ['Ana Lima', 'Bruno Souza', 'Carlos Melo', 'Diana Costa', 'Eduardo Reis',
                     'Fernanda Alves', 'Gabriel Nunes', 'Helena Pires', 'Igor Teixeira', 'Julia Rocha'],
    'estado': ['SP', 'RJ', 'MG', 'SP', 'RS', 'RJ', 'SP', 'MG', 'BA', 'SP']
}
df_clientes = pd.DataFrame(dados_clientes)

dados_produtos = {
    'id_produto': [101, 102, 103, 104, 105, 106],
    'nome_produto': ['Placa ESP32', 'Raspberry Pi 4', 'Orange Pi 4 LTS', 'Arduino Uno', 'SSD 480GB', 'Memória RAM 8GB'],
    'preco_unitario': [45.90, 450.00, 380.00, 85.50, 220.00, 180.00],
    'estoque': [150, 50, 30, 200, 75, 120]
}
df_produtos = pd.DataFrame(dados_produtos)

dados_vendas = {
    'id_venda':         [1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15],
    'id_cliente':       [1,   1,   2,   3,   3,   4,   5,   5,   6,   7,   7,   8,   9,  10,  10],
    'id_produto':       [101, 104, 103, 101, 106, 102, 104, 105, 101, 103, 104, 106, 102, 101, 105],
    'quantidade_comprada': [2,  1,   3,   5,   2,   1,   4,   1,   3,   2,   1,   2,   1,   6,   2]
}
df_vendas = pd.DataFrame(dados_vendas)

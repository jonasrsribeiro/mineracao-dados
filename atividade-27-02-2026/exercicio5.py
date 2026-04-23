import pandas as pd
import numpy as np

dados_motoristas = {
    'id_motorista': [1, 2, 3, 4, 5, 6],
    'nome_motorista': ['Carlos Andrade', 'Márcio Braga', 'Sandra Cunha', 'Roberto Faria', 'Tatiane Lopes', 'Valter Neves'],
    'cnh_categoria': ['E', 'D', 'D', 'E', 'D', 'E'],
    'anos_experiencia': [12, 7, 5, 15, 3, 9]
}
df_motoristas = pd.DataFrame(dados_motoristas)

dados_veiculos = {
    'id_veiculo': [10, 11, 12, 13, 14, 15, 16],
    'placa': ['ABC-1234', 'DEF-5678', 'GHI-9012', 'JKL-3456', 'MNO-7890', 'PQR-1357', 'STU-2468'],
    'tipo_veiculo': ['Caminhão', 'Van', 'Van', 'Caminhão', 'Moto', 'Van', 'Caminhão'],
    'capacidade_kg': [8000, 1500, 1500, 10000, 50, 1500, 12000]
}
df_veiculos = pd.DataFrame(dados_veiculos)

dados_entregas = {
    'id_entrega':   [1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24],
    'id_motorista': [1,   1,   2,   2,   3,   3,   4,   4,   5,   5,   6,   6,   1,   2,   3,   4,   5,   6,   1,   2,   3,   4,   5,   6],
    'id_veiculo':   [10,  11,  11,  12,  12,  11,  13,  10,  14,  15,  16,  13,  10,  12,  16,  13,  14,  10,  11,  16,  12,  10,  15,  16],
    'distancia_km': [320, 180, 210, 195, 165, 200, 450, 380, 55,  60,  290, 410, 300, 175, 220, 500, 45,  350, 260, 240, 185, 420, 50,  310],
    'status_entrega': ['Entregue', 'Entregue', 'Entregue', 'Entregue', 'Entregue', 'Entregue',
                       'Entregue', 'Entregue', 'Entregue', 'Em trânsito', 'Entregue', 'Entregue',
                       'Entregue', 'Entregue', 'Em trânsito', 'Entregue', 'Entregue', 'Entregue',
                       'Entregue', 'Em trânsito', 'Entregue', 'Entregue', 'Entregue', 'Entregue'],
    'data_entrega': pd.to_datetime(['2026-02-01', '2026-02-03', '2026-02-01', '2026-02-05', '2026-02-02', '2026-02-06',
                                    '2026-02-01', '2026-02-04', '2026-02-02', None, '2026-02-03', '2026-02-07',
                                    '2026-02-08', '2026-02-09', None, '2026-02-10', '2026-02-11', '2026-02-12',
                                    '2026-02-13', None, '2026-02-14', '2026-02-15', '2026-02-16', '2026-02-17'])
}
df_entregas = pd.DataFrame(dados_entregas)

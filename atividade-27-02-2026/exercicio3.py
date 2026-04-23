import pandas as pd
import numpy as np

dados_ambientes = {
    'id_ambiente': [1, 2, 3, 4, 5],
    'nome_setor': ['Fundição', 'Montagem', 'Almoxarifado', 'Escritório', 'Câmara Fria'],
    'descricao': ['Setor de fundição de metais', 'Linha de montagem principal',
                  'Armazenamento de materiais', 'Área administrativa', 'Armazenamento refrigerado']
}
df_ambientes = pd.DataFrame(dados_ambientes)

dados_dispositivos = {
    'id_dispositivo': [1, 2, 3, 4, 5, 6, 7, 8],
    'nome_dispositivo': ['RPI-F01', 'ESP32-F02', 'OPI-M01', 'ESP32-M02', 'RPI-A01', 'ESP32-E01', 'OPI-C01', 'ESP32-F03'],
    'tipo_dispositivo': ['Raspberry Pi 4', 'ESP32', 'Orange Pi 4 LTS', 'ESP32', 'Raspberry Pi 4', 'ESP32', 'Orange Pi 4 LTS', 'ESP32'],
    'id_ambiente': [1, 1, 2, 2, 3, 4, 5, 1]
}
df_dispositivos = pd.DataFrame(dados_dispositivos)

np.random.seed(42)
n = 80
id_dispositivos_lista = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8], size=n)

temp_base = {1: 45.0, 2: 42.0, 3: 35.0, 4: 28.0, 5: 38.0, 6: 22.0, 7: 2.0, 8: 44.0}
umid_base = {1: 60.0, 2: 62.0, 3: 55.0, 4: 58.0, 5: 50.0, 6: 45.0, 7: 85.0, 8: 61.0}

temperaturas = np.array([temp_base[d] + np.random.uniform(-3, 3) for d in id_dispositivos_lista])
umidades = np.array([umid_base[d] + np.random.uniform(-5, 5) for d in id_dispositivos_lista])

datas = pd.date_range(start='2026-02-01 06:00', periods=n, freq='3h')

dados_telemetria = {
    'id_telemetria': np.arange(1, n + 1),
    'id_dispositivo': id_dispositivos_lista,
    'data_hora': datas,
    'temperatura_c': np.round(temperaturas, 2),
    'umidade_pct': np.round(umidades, 2)
}
df_telemetria = pd.DataFrame(dados_telemetria)

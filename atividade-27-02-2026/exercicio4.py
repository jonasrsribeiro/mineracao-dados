import pandas as pd
import numpy as np

dados_usuarios = {
    'id_usuario': [1, 2, 3, 4, 5, 6, 7, 8],
    'nome_usuario': ['Ana Paula', 'Bruno Ferreira', 'Carla Dias', 'Daniel Mota',
                     'Elaine Torres', 'Felipe Gomes', 'Gabriela Silva', 'Hugo Cardoso'],
    'departamento': ['RH', 'Financeiro', 'TI', 'Operações', 'RH', 'Financeiro', 'Operações', 'TI']
}
df_usuarios = pd.DataFrame(dados_usuarios)

dados_equipamentos = {
    'id_equipamento': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    'nome_equipamento': ['Desktop-RH01', 'Desktop-FIN01', 'Notebook-TI01', 'Desktop-OP01',
                         'Notebook-RH02', 'Desktop-FIN02', 'Desktop-OP02', 'Notebook-TI02',
                         'Desktop-RH03', 'Desktop-FIN03'],
    'sistema_operacional': ['Windows 10', 'Windows 11', 'Ubuntu 22.04', 'Windows 10',
                            'Windows 11', 'Windows 10', 'Windows 11', 'Ubuntu 22.04',
                            'Windows 10', 'Windows 11'],
    'id_usuario': [1, 2, 3, 4, 5, 6, 7, 8, 1, 2]
}
df_equipamentos = pd.DataFrame(dados_equipamentos)

dados_chamados = {
    'id_ticket':       [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018],
    'id_usuario':      [1,    2,    3,    4,    5,    6,    7,    8,    1,    2,    3,    4,    5,    6,    7,    8,    1,    3],
    'id_equipamento':  [10,   11,   12,   13,   14,   15,   16,   17,   10,   11,   12,   13,   14,   15,   16,   17,   18,   19],
    'categoria':       ['Hardware', 'Software', 'Rede', 'Hardware', 'Software', 'Hardware', 'Rede', 'Software',
                        'Software', 'Hardware', 'Rede', 'Software', 'Hardware', 'Rede', 'Software', 'Hardware', 'Rede', 'Software'],
    'status':          ['Fechado', 'Fechado', 'Aberto', 'Fechado', 'Fechado', 'Fechado', 'Aberto', 'Fechado',
                        'Fechado', 'Aberto', 'Fechado', 'Fechado', 'Fechado', 'Fechado', 'Aberto', 'Fechado', 'Fechado', 'Aberto'],
    'horas_resolucao': [2.0, 1.5, 0.0, 4.0, 3.5, 2.5, 0.0, 1.0, 5.0, 0.0, 3.0, 2.0, 4.5, 1.5, 0.0, 6.0, 2.0, 0.0]
}
df_chamados = pd.DataFrame(dados_chamados)

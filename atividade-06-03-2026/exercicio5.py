import pandas as pd

dados = {
    'ID_Veiculo': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Proprietario': ['Ana Lima', 'Bruno Souza', 'Carlos Melo', 'Diana Costa', 'Eduardo Reis',
                     'Fernanda Alves', 'Gabriel Nunes', 'Helena Pires', 'Igor Teixeira', 'Julia Rocha'],
    'Placa_Veiculo': ['ABC1234', 'DEF5678', 'GHI901', 'JKL3456', 'MNO78902',
                      'PQR1357', 'STU246', 'VWX9012', 'YZA-3456', 'BCD5678']
}

df = pd.DataFrame(dados)

placas_invalidas = df[df['Placa_Veiculo'].str.len() != 7]

print("Dados originais:")
print(df)
print("\nVeículos com placa de tamanho incorreto:")
print(placas_invalidas)

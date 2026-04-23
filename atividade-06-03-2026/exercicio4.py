import pandas as pd

dados = {
    'ID_Equipamento': range(1, 41),
    'Sistema_Operacional': [
        'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu',
        'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu', 'Ubuntu',
        'Debian', 'Debian', 'Debian', 'Debian', 'Debian', 'Debian', 'Debian', 'Debian', 'Debian', 'Debian',
        'Armbian', 'Armbian', 'Armbian', 'Armbian', 'Armbian', 'Armbian',
        'Ubuntuu', 'Debiann', 'ArmBian', 'Ubunto'
    ]
}

df = pd.DataFrame(dados)

proporcao = df['Sistema_Operacional'].value_counts(normalize=True) * 100

raros = proporcao[proporcao < 5]

print("Proporção de cada Sistema Operacional (%):")
print(proporcao)
print("\nCategorias que representam menos de 5% dos dados (possíveis erros de digitação):")
print(raros)

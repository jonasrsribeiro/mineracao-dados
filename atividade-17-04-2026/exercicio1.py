import pandas as pd

df = pd.DataFrame({
    'Usuario': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda'],
    'Email': [
        'ana@gmail.com',
        'bruno@empresa.com.br',
        'carlos@yahoo.com',
        'ti@fabricaindoor.com.br',
        'eduardo@hotmail.com',
        'vendas@distribuidora.com.br'
    ]
})

print("Dados brutos:")
print(df, "\n")

df['Dominio'] = df['Email'].str.split('@').str[1]

df['Flag_Corporativo'] = df['Dominio'].str.endswith('.com.br').astype(int)

print("Após engenharia de texto:")
print(df[['Usuario', 'Email', 'Dominio', 'Flag_Corporativo']])

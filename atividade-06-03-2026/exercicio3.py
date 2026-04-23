import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    'Nome':         ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Flávia', 'Gustavo', 'Helena', 'Igor', 'Julia'],
    'Email':        ['ana@email.com', np.nan, 'carlos@email.com', np.nan, 'edu@email.com',
                     np.nan, np.nan, 'helena@email.com', np.nan, 'julia@email.com'],
    'Telefone':     ['9999-1111', '8888-2222', np.nan, '7777-3333', np.nan,
                     '6666-4444', '5555-5555', np.nan, '4444-6666', np.nan],
    'Departamento': ['TI', 'RH', np.nan, 'TI', 'Financeiro',
                     np.nan, 'RH', 'TI', np.nan, 'Financeiro'],
    'Cargo':        [np.nan, 'Analista', 'Gerente', np.nan, 'Analista',
                     'Técnico', np.nan, 'Gerente', 'Analista', np.nan],
    'Salario':      [3500, np.nan, 8000, 4200, np.nan,
                     3100, 3800, np.nan, 4500, np.nan]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title('Mapa de Calor - Valores Ausentes no Formulário')
plt.tight_layout()
plt.show()

print("Porcentagem de nulos por coluna:")
print(df.isnull().mean() * 100)

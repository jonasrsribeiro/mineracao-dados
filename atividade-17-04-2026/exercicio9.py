import pandas as pd

df = pd.DataFrame({
    'ID_Acesso': range(1, 13),
    'Usuario':   ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda',
                  'Gabriel', 'Helena', 'Igor', 'Julia', 'Karen', 'Lucas'],
    'Hora':      [2, 5, 8, 11, 13, 16, 18, 20, 22, 0, 3, 14]
})

print("Dados brutos com hora numérica:")
print(df, "\n")

bins   = [-1, 5, 11, 17, 23]
labels = ['Madrugada', 'Matutino', 'Comercial', 'Noite']

df['Turno'] = pd.cut(df['Hora'], bins=bins, labels=labels)

print("Após categorização em turnos:")
print(df)

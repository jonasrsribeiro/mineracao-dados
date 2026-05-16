import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("titles.csv")
# variáveis 
X = df[["release_year"]] 
y = df["type"] 
# divisão treino/teste 
X_train, X_test, y_train, y_test = train_test_split( 
X, y, 
test_size=0.3, 
random_state=42 
) 
# Grupo 3 - Regressão Logística
model = LogisticRegression()
# ========================= 
# TREINAMENTO E TESTE 
# ========================= 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
acc = accuracy_score(y_test, y_pred) 
print("Acurácia:", acc)
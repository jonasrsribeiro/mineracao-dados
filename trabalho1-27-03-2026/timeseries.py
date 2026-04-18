import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.impute import KNNImputer

datas = pd.date_range("2024-01-01", periods=10, freq="D")
valores_reais = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]  # progressão perfeita
valores_com_nan = [10, np.nan, 14, np.nan, 18, 20, np.nan, 24, 26, 28]

df = pd.DataFrame({"valor_original": valores_com_nan}, index=datas)

print("=" * 60)
print("SÉRIE ORIGINAL COM DADOS AUSENTES")
print("=" * 60)
print(df.to_string())
print(f"\nTotal de NaN: {df['valor_original'].isna().sum()} de {len(df)} registros\n")

# 2. TÉCNICA 1 — FORWARD FILL (ffill)

df["ffill"] = df["valor_original"].ffill()

# 3. TÉCNICA 2 — INTERPOLAÇÃO LINEAR - Estima um valor proporcional entre os dois pontos conhecidos

df["interpolacao"] = df["valor_original"].interpolate(method="linear")

# 4. TÉCNICA 3 — KNN IMPUTER - Usa os k vizinhos mais próximos para estimar o valor ausente

knn = KNNImputer(n_neighbors=2)
df["knn"] = knn.fit_transform(df[["valor_original"]])

# 5. TABELA COMPARATIVA

print("=" * 60)
print("COMPARAÇÃO DAS TÉCNICAS")
print("=" * 60)
df["valor_real"] = valores_reais
print(df[["valor_original", "ffill", "interpolacao", "knn", "valor_real"]].to_string())

# Erro médio absoluto apenas nos pontos que eram NaN
nan_idx = df["valor_original"].isna()
print("\nErro Médio Absoluto (apenas nos pontos imputados):")
for col in ["ffill", "interpolacao", "knn"]:
    mae = (df.loc[nan_idx, col] - df.loc[nan_idx, "valor_real"]).abs().mean()
    print(f"  {col:15s}: MAE = {mae:.2f}")

# 6. VISUALIZAÇÃO

fig, axes = plt.subplots(2, 2, figsize=(14, 8), facecolor="#F0F6FA")
fig.suptitle(
    "Tratamento de Dados Ausentes em Séries Temporais\nComparação de Técnicas de Imputação",
    fontsize=14, fontweight="bold", color="#0A1F3D", y=1.01
)

NAVY, MINT, TEAL, RED = "#0A1F3D", "#00B4D8", "#1C7293", "#E05252"
cores = {"ffill": "#1255A0", "interpolacao": TEAL, "knn": "#8B5CF6"}

configs = [
    ("ffill",        "Forward Fill",        cores["ffill"]),
    ("interpolacao", "Interpolação Linear", cores["interpolacao"]),
    ("knn",          "KNN Imputer (k=2)",   cores["knn"]),
]

for ax, (col, titulo, cor) in zip(axes.flat[:3], configs):
    ax.set_facecolor("white")
    # linha do valor real (referência)
    ax.plot(df.index, df["valor_real"], color="gray", linestyle="--",
            linewidth=1.2, alpha=0.5, label="Valor real")
    # série com NaN
    ax.plot(df.index, df["valor_original"], "o", color=NAVY,
            markersize=7, label="Observado", zorder=5)
    # série imputada
    ax.plot(df.index, df[col], "-", color=cor, linewidth=2, label=titulo, zorder=4)
    # marcadores nos pontos imputados
    ax.plot(df.index[nan_idx], df.loc[nan_idx, col], "^",
            color=MINT, markersize=9, label="Imputado", zorder=6)
    ax.set_title(titulo, fontweight="bold", color=NAVY)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
    ax.legend(fontsize=8)
    ax.grid(axis="y", alpha=0.3)
    ax.set_ylim(6, 32)

# painel 4: comparação MAE
ax4 = axes[1][1]
ax4.set_facecolor("white")
tecnicas = ["ffill", "interpolacao", "knn"]
labels = ["Forward Fill", "Interpolação", "KNN (k=2)"]
maes = [(df.loc[nan_idx, t] - df.loc[nan_idx, "valor_real"]).abs().mean() for t in tecnicas]
bars = ax4.bar(labels, maes, color=[cores[t] for t in tecnicas], edgecolor="white", linewidth=1.2)
for bar, mae in zip(bars, maes):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
             f"{mae:.2f}", ha="center", va="bottom", fontweight="bold", color=NAVY)
ax4.set_title("Erro Médio Absoluto (MAE)\nnos pontos imputados", fontweight="bold", color=NAVY)
ax4.set_ylabel("MAE")
ax4.set_ylim(0, max(maes) * 1.3)
ax4.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("resultado_imputacao.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nGráfico salvo como 'resultado_imputacao.png'")

"""
Exercicio 2 - Exemplo Real: Analise de Sentimentos em Reviews da Steam
Aplica LeIA em 500 reviews em portugues coletados via API publica da Steam.
"""

import pandas as pd
from LeIA import SentimentIntensityAnalyzer
from langdetect import detect, LangDetectException

CSV_FILE = "reviews_steam_ptbr.csv"
COLUNA_TEXTO = "review"

analisador = SentimentIntensityAnalyzer()

PALAVRAS_NSFW = [
    "penis", "pênis", "pica", "pau", "buceta", "cu ", " cu\n", "sexo",
    "foder", "foda", "fodendo", "transar", "vagina", "tesao", "tesão",
    "pornô", "porno", "nude", "nudes", "putaria", "safado", "safada",
    "cuzao", "cuzão", "viado", "piroca",
]


def eh_portugues(texto):
    if not isinstance(texto, str) or len(texto.strip()) < 10:
        return True
    try:
        return detect(texto) == "pt"
    except LangDetectException:
        return True


def contem_nsfw(texto):
    if not isinstance(texto, str):
        return False
    t = texto.lower()
    return any(p in t for p in PALAVRAS_NSFW)


def classificar(texto):
    if not isinstance(texto, str) or texto.strip() == "":
        return "NEUTRA"
    compound = analisador.polarity_scores(texto)["compound"]
    if compound >= 0.05:
        return "POSITIVA"
    elif compound <= -0.05:
        return "NEGATIVA"
    else:
        return "NEUTRA"


def main():
    print(f"\nCarregando dataset: {CSV_FILE}")
    df = pd.read_csv(CSV_FILE, encoding="utf-8-sig")
    df[COLUNA_TEXTO] = df[COLUNA_TEXTO].astype(str).str.replace(r"[\r\n]+", " ", regex=True).str.strip()
    print(f"Total de reviews carregados: {len(df)}")

    antes = len(df)
    df = df[~df[COLUNA_TEXTO].apply(contem_nsfw)].reset_index(drop=True)
    print(f"Reviews apos filtro de conteudo: {len(df)} ({antes - len(df)} removidos)")

    antes = len(df)
    df = df[df[COLUNA_TEXTO].apply(eh_portugues)].reset_index(drop=True)
    print(f"Reviews apos filtro de idioma:   {len(df)} ({antes - len(df)} removidos)\n")

    print("Aplicando LeIA em toda a coluna de reviews...")
    df["sentimento"] = df[COLUNA_TEXTO].apply(classificar)

    contagem = df["sentimento"].value_counts()
    total = len(df)

    print("\n" + "="*50)
    print("    RESULTADO DA ANALISE DE SENTIMENTOS")
    print("    Reviews da Steam em Portugues (CS2)")
    print("="*50)
    for categoria in ["POSITIVA", "NEGATIVA", "NEUTRA"]:
        qtd = contagem.get(categoria, 0)
        pct = (qtd / total) * 100
        barra = "#" * int(pct / 2)
        print(f"  {categoria:<10}: {qtd:>5} reviews  ({pct:.1f}%)  {barra}")
    print(f"  {'TOTAL':<10}: {total:>5} reviews")
    print("="*50)

    output_file = "resultado_sentimentos.csv"
    df[[COLUNA_TEXTO, "sentimento"]].to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"\nResultado salvo em: {output_file}")

    print("\nAmostra de reviews classificados (2 positivas, 1 neutra, 2 negativas):")
    amostra = pd.concat([
        df[df["sentimento"] == "POSITIVA"].sample(2),
        df[df["sentimento"] == "NEUTRA"].sample(1),
        df[df["sentimento"] == "NEGATIVA"].sample(2),
    ]).reset_index(drop=True)
    amostra[COLUNA_TEXTO] = amostra[COLUNA_TEXTO].apply(
        lambda x: x.encode("cp1252", errors="replace").decode("cp1252") if isinstance(x, str) else x
    )
    print(amostra[[COLUNA_TEXTO, "sentimento"]].to_string(index=False))


if __name__ == "__main__":
    main()

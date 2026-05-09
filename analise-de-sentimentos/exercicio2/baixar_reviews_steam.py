"""
Baixa reviews em portugues direto da API publica da Steam e salva como CSV.
Nao precisa de autenticacao nem web scraping.
"""

import requests
import pandas as pd
import time

# Counter-Strike 2 (730) - jogo com muitos reviews em portugues
APP_ID = 730
TOTAL_REVIEWS = 500
SAIDA_CSV = "reviews_steam_ptbr.csv"


def buscar_reviews(app_id, cursor="*", qtd=100):
    url = f"https://store.steampowered.com/appreviews/{app_id}"
    params = {
        "json": 1,
        "language": "brazilian",
        "review_type": "all",
        "purchase_type": "all",
        "num_per_page": qtd,
        "cursor": cursor,
        "filter": "recent",
    }
    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


def main():
    print(f"Buscando {TOTAL_REVIEWS} reviews em portugues do app {APP_ID} na Steam...")
    todos = []
    cursor = "*"

    while len(todos) < TOTAL_REVIEWS:
        faltam = TOTAL_REVIEWS - len(todos)
        qtd = min(100, faltam)
        dados = buscar_reviews(APP_ID, cursor=cursor, qtd=qtd)

        reviews = dados.get("reviews", [])
        if not reviews:
            print("Sem mais reviews disponiveis.")
            break

        for r in reviews:
            todos.append({
                "review": r["review"],
                "recomendado": r["voted_up"],
                "votos_uteis": r["votes_up"],
            })

        cursor = dados.get("cursor", "*")
        print(f"  Coletados: {len(todos)} reviews...")
        time.sleep(0.5)

    df = pd.DataFrame(todos)
    df.to_csv(SAIDA_CSV, index=False, encoding="utf-8-sig")
    print(f"\nSalvo: {SAIDA_CSV}  ({len(df)} reviews)")
    print(df.head(3).to_string(index=False))


if __name__ == "__main__":
    main()

from LeIA import SentimentIntensityAnalyzer

analisador = SentimentIntensityAnalyzer()


def analisar(frase):
    scores = analisador.polarity_scores(frase)
    compound = scores["compound"]
    if compound >= 0.05:
        polaridade = "POSITIVA"
    elif compound <= -0.05:
        polaridade = "NEGATIVA"
    else:
        polaridade = "NEUTRA"
    return scores, polaridade


def exibir_resultado(rotulo, frase):
    scores, polaridade = analisar(frase)
    print(f"\n{'='*60}")
    print(f"[{rotulo}]")
    print(f"Frase: \"{frase}\"")
    print(f"  Compound (Polaridade): {scores['compound']:+.4f}  =>  {polaridade}")
    print(f"  Positivo: {scores['pos']:.4f} | Negativo: {scores['neg']:.4f} | Neutro: {scores['neu']:.4f}")
    print(f"{'='*60}")


print("\n>>> ANALISE DIDATICA DE SENTIMENTOS <<<")
print("Biblioteca: LeIA (versao portuguesa do VADER)\n")

exibir_resultado(
    "POSITIVA",
    "gostei muito do jogo, excelente e maravilhoso!"
)

exibir_resultado(
    "NEGATIVA",
    "Jogo horrivel e ruim, cheio de bugs e erros."
)

frase_base   = "O jogo e excelente, gostei muito."
frase_negada = "O jogo nao e excelente, nao gostei muito nao."

scores_base,   pol_base   = analisar(frase_base)
scores_negada, pol_negada = analisar(frase_negada)

print(f"\n{'='*60}")
print("[NEGACAO - Comparativo]")
print(f"  Sem negacao : \"{frase_base}\"")
print(f"  Compound    : {scores_base['compound']:+.4f}  =>  {pol_base}")
print()
print(f"  Com negacao : \"{frase_negada}\"")
print(f"  Compound    : {scores_negada['compound']:+.4f}  =>  {pol_negada}")
print()
print("  >>> O 'nao' reduziu o score positivo,")
print("      mostrando que o algoritmo reconhece o modificador.")
print(f"{'='*60}")

exibir_resultado(
    "SARCASMO - Teste de Estresse",
    "Que otimo jogo! So trava e perde meu progresso. Perfeito."
)

print("\n\n--- DEBATE: TESTE DE ESTRESSE COM SARCASMO ---")
print("A frase sarcastica contem palavras positivas ('otimo', 'perfeito')")
print("que enganam o algoritmo lexico.")
print("O LeIA retorna POSITIVO, mas o sentimento real e NEGATIVO.")
print("Esse e o principal limite dos sistemas baseados em dicionarios:")
print("eles nao entendem contexto nem ironia.")

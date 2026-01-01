# ============================================================
# Mini-Projet P1-C1 : Cryptanalyse intelligente automatique
# ============================================================
# Objectif : Retrouver automatiquement le texte clair
#            à partir d'un message chiffré sans connaître la clé
# ============================================================


# -----------------------------
# Fonction 1 : Déchiffrement César
# -----------------------------
def dechiffrement_cesar(texte_chiffre, cle):
    """
    Cette fonction applique un déchiffrement de César
    en décalant chaque lettre de 'cle' positions vers l'arrière.
    """
    texte_clair = ""

    for caractere in texte_chiffre:
        # Vérifier si le caractère est une lettre
        if caractere.isalpha():
            # Déterminer si la lettre est majuscule ou minuscule
            base = ord('A') if caractere.isupper() else ord('a')

            nouvelle_lettre = chr((ord(caractere) - base - cle) % 26 + base)

            texte_clair += nouvelle_lettre
        else:
            texte_clair += caractere

    return texte_clair


# -----------------------------
# Fonction 2 : Évaluation linguistique
# -----------------------------
def score_linguistique(texte):
    """
    Cette fonction attribue un score au texte
    en fonction de la présence de mots français courants.
    """
    mots_frequents = [
        " le ", " de ", " la ", " et ", " que ",
        " un ", " une ", " est ", " pour ", " dans "
    ]

    score = 0
    texte_minuscule = texte.lower()

    # Compter les occurrences de mots fréquents
    for mot in mots_frequents:
        score += texte_minuscule.count(mot)

    return score


# -----------------------------
# Fonction 3 : Cryptanalyse automatique
# -----------------------------
def cryptanalyse_cesar(texte_chiffre):
    """
    Cette fonction teste toutes les clés possibles,
    évalue les résultats et sélectionne le meilleur.
    """
    meilleurs_resultats = []

    # Tester toutes les clés possibles (0 à 25)
    for cle in range(26):
        texte_dechiffre = dechiffrement_cesar(texte_chiffre, cle)
        score = score_linguistique(texte_dechiffre)

        meilleurs_resultats.append((cle, score, texte_dechiffre))

    # Trier les résultats par score décroissant
    meilleurs_resultats.sort(key=lambda x: x[1], reverse=True)

    return meilleurs_resultats

# -----------------------------
# Programme principal
# -----------------------------
if __name__ == "__main__":

    print("=" * 60)
    print("        CRYPTANALYSE INTELLIGENTE AUTOMATIQUE")
    print("                Mini-Projet P1-C1")
    print("=" * 60)

    # Message chiffré
    message_chiffre = "Ohd vhfxulwh lqirupdwltxh hvw hvvhqwlhobh"

    print("\n📩 Message chiffré intercepté :")
    print("   ", message_chiffre)

    print("\n🔍 Analyse en cours...")
    print("   Test de toutes les clés possibles (0 à 25)")
    print("   Évaluation linguistique de chaque résultat\n")

    resultats = cryptanalyse_cesar(message_chiffre)

    # Meilleur résultat
    meilleure_cle, meilleur_score, meilleur_texte = resultats[0]

    print("=" * 60)
    print("✅ RÉSULTAT LE PLUS PROBABLE")
    print("=" * 60)
    print(f"🔑 Clé trouvée        : {meilleure_cle}")
    print(f"📊 Score linguistique : {meilleur_score}")
    print("📜 Texte clair :")
    print("   ", meilleur_texte)

    print("\n" + "=" * 60)
    print("📌 AUTRES HYPOTHÈSES CRÉDIBLES")
    print("=" * 60)

    for cle, score, texte in resultats[1:6]:
        print(f"🔸 Clé {cle:2d} | Score {score:2d} | {texte}")

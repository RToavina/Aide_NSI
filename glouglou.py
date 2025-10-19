def glouglou(chaine):
    """Renvoie une chaîne de caractères transformée selon la règle du "glouglou"."""
    voyelle = "aeiouyAEIOUY"
    resultat = ""
    for caractere in chaine:
        if caractere in voyelle:
            resultat += caractere+caractere
        else:
            resultat += caractere
    return resultat

# Exemple d'utilisation
if __name__ == "__main__":
    texte = "allez toulon"
    print(glouglou(texte))
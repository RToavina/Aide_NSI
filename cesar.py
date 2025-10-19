def cesar(chaine, decalage):
    """Applique un chiffrement de César à une chaîne de caractères."""
    resultat = ""

    for caractere in chaine:
        # Vérifie si le caractère est une lettre
        if caractere.isalpha():
            # Détermine l'offset ASCII en fonction de la casse
            ascii_offset = ord('A') if caractere.isupper() else ord('a')
            # Décale le caractère et gère le wrap-around
            caractere_decale = chr((ord(caractere) - ascii_offset + decalage) % 26 + ascii_offset)
            resultat += caractere_decale
        else:
            resultat += caractere

    return resultat

# Exemple d'utilisation
if __name__ == "__main__":
    texte = "Bonjour, Monde!"
    decalage = 3
    texte_chiffre = cesar(texte, decalage)
    print(f"Texte original: {texte}")
    print(f"Texte chiffré avec un décalage de {decalage}: {texte_chiffre}")
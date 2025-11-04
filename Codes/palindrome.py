def palindrome(chaine):
    """Renvoie True si la chaîne de caractères est un palindrome, False sinon.

    Args:
        chaine (str): La chaîne de caractères à vérifier.

    Returns:
        bool: True si la chaîne est un palindrome, False sinon.
    """
    chaine = chaine.replace(" ", "").lower()  # Ignorer les espaces et la casse
    longueur = len(chaine)
    for i in range(longueur // 2):
        if chaine[i] != chaine[longueur - 1 - i]:
            return False
    return True

# Exemple d'utilisation
if __name__ == "__main__":
    texte = "Anna"
    print(palindrome(texte))  # Devrait afficher True
    texte2 = "Bonjour" 
    print(palindrome(texte2))  # Devrait afficher False
    
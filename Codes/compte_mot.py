def compte_mot(texte):
    """Compte le nombre de mots dans une chaîne de caractères.

    Args:
        texte (str): La chaîne de caractères à analyser.

    Returns:
        int: Le nombre de mots dans la chaîne.
    """
    # On utilise la méthode split pour diviser le texte en mots
    mots = texte.split()
    # Le nombre de mots est la longueur de la liste obtenue
    return len(mots)

# Exemple d'utilisation
if __name__ == "__main__":
    texte = "Bonjour tout le monde"
    print(compte_mot(texte))
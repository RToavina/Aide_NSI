def vertical(chaine):
    """Renvoie une chaîne de caractères écrite verticalement.

    Args:
        chaine (str): La chaîne de caractères à écrire verticalement.

    Returns:
        str: La chaîne de caractères écrite verticalement, avec chaque caractère
             sur une nouvelle ligne.
    """
    resultat = ""
    #version for
    for caractere in chaine:
        resultat += caractere + "\n"

    #version while
    # i = 0
    # while i < len(chaine):
    #     resultat += chaine[i] + "\n"
    #     i += 1

    return resultat

# Exemple d'utilisation
if __name__ == "__main__":
    texte = "Bonjour"
    print(vertical(texte))
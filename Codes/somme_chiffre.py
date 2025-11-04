def somme_chiffre(n):
    """
    Calcule la somme des chiffres d'un nombre entier n.

    Args:
        n (int): Un nombre entier dont on veut calculer la somme des chiffres.

    Returns:
        int: La somme des chiffres de n.
    """
    # Convertir le nombre en chaîne de caractères pour itérer sur chaque chiffre
    chiffres = str(abs(n))  # Utiliser abs pour gérer les nombres négatifs
    somme = 0

    # Itérer sur chaque caractère dans la chaîne et additionner les valeurs entières
    for chiffre in chiffres:
        somme += int(chiffre)

    return somme

# Exemple d'utilisation
if __name__ == "__main__":
    nombre = 12345
    print(somme_chiffre(nombre))  # Devrait afficher 15
    nombre2 = -6789
    print(somme_chiffre(nombre2))  # Devrait afficher 30
    nombre3 = 0
    print(somme_chiffre(nombre3))  # Devrait afficher 0
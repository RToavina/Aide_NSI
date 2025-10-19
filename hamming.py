def hamming(chaine1,chaine2):
    """Calcul la distance de Hamming entre deux chaînes de caractères.

    La distance de Hamming est définie comme le nombre de positions
    auxquelles les symboles correspondants sont différents.

    Args:
        chaine1 (str): La première chaîne de caractères.
        chaine2 (str): La deuxième chaîne de caractères.

    Returns:
        int: La distance de Hamming entre les deux chaînes.

    Raises:
        ValueError: Si les deux chaînes n'ont pas la même longueur.
    """
    if len(chaine1) != len(chaine2):
        raise ValueError("Les chaînes doivent avoir la même longueur.")

    distance = 0
    for char1, char2 in zip(chaine1, chaine2): #zip permet de parcourir les deux chaînes en parallèle
        if char1 != char2:
            distance += 1

    return distance

# Exemple d'utilisation
if __name__ == "__main__":
    chaine_a = "karolin"
    chaine_b = "kathrin"
    print(hamming(chaine_a, chaine_b))  # Devrait afficher 3
    chaine_c = "karolin"
    chaine_d = "kerstin"
    print(hamming(chaine_c, chaine_d))  # Devrait afficher 3
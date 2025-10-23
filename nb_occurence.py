def nb_occurence(n,tab):
    """

    Cette fonction prend en entrée un entier n et une liste tab,
    et retourne le nombre d'occurrences de n dans tab.

    :param n: entier à rechercher
    :param tab: liste d'entiers
    :return: nombre d'occurrences de n dans tab

    """
    compteur = 0
    for element in tab:
        if element == n:
            compteur += 1

    return compteur

#Exemple d'utilisation
print(nb_occurence(1,[1,3,5,1,1,1,5])) #réponse attendue 4


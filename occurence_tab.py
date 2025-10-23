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

def occurence_tab(tab):
    """
    Cette fonction prend en entrée une liste tab,
    et retourne l'element qui a le plus d'occurrences dans tab
    en utilisant la fonction nb_occurence.
    """

    max_occurrences = 0
    element_max = None

    for element in tab:
        occurrences = nb_occurence(element, tab)
        if occurrences > max_occurrences:
            max_occurrences = occurrences
            element_max = element

    return element_max

#Exemple d'utilisation
print(occurence_tab([1,3,5,1,1,1,5])) #réponse attendue 1
print(occurence_tab([2,2,3,3,3,4,4,4,4])) #réponse attendue 4
print(occurence_tab([5,5,5,6,6,7])) #réponse attendue 5




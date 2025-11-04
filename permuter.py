def permuter(tab):
    """
    On souhaite permuter tous les éléments dans une liste de listes. Pour cela écrire une fonction permuter(tab) qui renvoie une liste de listes où pour chaque élément de tab, vous aurez permuter son numéro de ligne avec son numéro de colonne.

    Par exemple, l’élément qui se trouve dans la colonne 2 et sur la ligne 3 dans tab devra se retrouver dans la colonne 3 et sur la ligne 2 dans la liste de listes retournée.

    permuter(tab) :

    paramètre :
    tab : Liste de listes pouvant contenir du éléments de type int, float ou str.
    Valeur retournée :
    result : Liste de listes pouvant contenir du éléments de type int, float ou str.
    """

    if not tab or not tab[0]:
        return []

    rows = len(tab)
    cols = len(tab[0])
    result = [[None] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = tab[i][j]

    return result

# Exemple d'utilisation
if __name__ == "__main__":
    tab = [[1,2],[3,4],[5,6]]
    print(permuter(tab))
    # Output: [[1, 3, 5], [2, 4, 6]]
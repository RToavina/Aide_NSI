def supprime_total(n, liste):
    """Supprime toutes les occurrences de n dans la liste.

    Args:
        n: L'élément à supprimer.
        liste: La liste dans laquelle supprimer les occurrences de n.

    Returns:
        list: La liste après suppression des occurrences de n.
    """
    resultat = []
    for element in liste:
        if element != n:
            resultat.append(element)
    return resultat
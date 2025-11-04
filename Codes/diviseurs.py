def diviseur(n):
    """Renvoie la liste des diviseurs de n.

    Args:
        n (int): Un entier positif.

    Returns:
        list: La liste des diviseurs de n.
    """
    diviseurs = []
    for i in range(1, n + 1):
        if n % i == 0:
            diviseurs.append(i)
    return diviseurs

    # # Equivalent while
    # diviseurs = []
    # i = 1
    # while i <= n:
    #     if n % i == 0:
    #         diviseurs.append(i)
    #     i += 1
    # return diviseurs
    

# Exemple d'utilisation
print(diviseur(12))  # Devrait afficher [1, 2, 3, 4, 6, 12]


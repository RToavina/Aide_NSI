def pascal(n):
    """ Génère le triangle de Pascal jusqu'à la n-ième ligne. 
    Args:
        n (int): Le nombre de lignes du triangle de Pascal à générer.
        Returns:
        list: Une liste de listes représentant le triangle de Pascal.
    """
    triangle = []
    for i in range(n):
        ligne = [1] * (i + 1)
        for j in range(1, i):
            ligne[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(ligne)
    return triangle

def affiche_pascal(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(len(triangle[-1]) * 2))

# Example usage:
n = 5
affiche_pascal(pascal(n))
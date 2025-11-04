from random import randint

def mon_tableau(ligne,colonne0):
    """
    Cette fonction crée un tableau à deux dimensions de taille ligne x colonne 
    rempli de nombres aléatoires entre 1 et 9.
    """
    tableau = []

    
    ##Equivalent for 
    #for i in range(ligne):
    #    ligne = []
    #    for j in range(colonne0):
    #        ligne.append(randint(1,9))
    #    tableau.append(ligne)
    
    ##Equivalent while
    i = 0
    while i < ligne:
        ligne = []
        j = 0
        while j < colonne0:
            ligne.append(randint(1,9))
            j += 1
        tableau.append(ligne)
        i += 1

    return tableau

# Exemple d'utilisation
if __name__ == "__main__":
    ligne = 3
    colonne0 = 4
    tableau = mon_tableau(ligne, colonne0)
    for ligne in tableau:
        print(ligne)


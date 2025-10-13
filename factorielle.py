def factorielle(n):

    #Equivalent boucle while
    i = 1
    resultat = 1
    if n == 0:
        return resultat
    while i < n:
        resultat *= i+1
        i += 1
    return resultat

    # #Equivalent boucle for
    # for i in range(1, n):
    #     n *= i

    # return n

#Test de la fonction
n = int(input("Entrez un nombre n pour calculer sa factorielle : "))
print("La factorielle de", n, "est", factorielle(n))
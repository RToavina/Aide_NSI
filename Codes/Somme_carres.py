def somme_carres(n):
    #Equivalent boucle while
    i = 1
    resultat = 0
    while i <= n:
        resultat += i**2
        i += 1
    return resultat

    # #Equivalent boucle for
    # resultat = 0
    # for i in range(1, n+1):
    #     resultat += i**2
    # return resultat

#Test de la fonction   
n = int(input("Entrez un nombre n pour calculer la somme des carrés jusqu'à n : "))
print("La somme des carrés jusqu'à", n, "est", somme_carres(n))


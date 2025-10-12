def estPremier(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def afficher_n_premier(n):
    compteur = 0
    nombre = 2

    #Equivalent boucle while
    while compteur < n:
        if estPremier(nombre):
            print(nombre)
            compteur += 1
        nombre += 1
    
    # #Equivalent boucle for
    # for nombre in range(2, 1000): #On met une limite haute arbitraire
    #     if compteur < n:
    #         if estPremier(nombre):
    #             print(nombre)
    #             compteur += 1
    #     else:
    #         break

#Test de la fonction
afficher_n_premier(100)
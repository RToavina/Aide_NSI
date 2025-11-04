def estPremier(n):
    if n < 2:
        return False
    
    #Equivalent boucle while
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1

    # #Equivalent boucle for
    # for i in range(2, n):
    #     if n % i == 0:
    #         return False
        
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
n = int(input("Entrez un nombre n pour afficher les n premiers nombres premiers : "))
afficher_n_premier(n)
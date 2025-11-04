def table_multiplication(n):
    """ Génère une table de multiplication de 0 à 10 pour un nombre donné n. """
    #Equivalent for
    for i in range(11):
        print(f"{n} x {i} = {n * i}")

    # #Equivalent while
    # i = 0
    # while i <= 10:
    #     print(f"{n} x {i} = {n * i}")
    #     i += 1

# Exemple d'utilisation
table_multiplication(5)

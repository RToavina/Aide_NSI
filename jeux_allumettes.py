joueur = str(input("Donner le nom du joueur : "))
cpu = "Ordinateur"

nombres_allumettes = int(input("Donner le nombre d'allumettes avec lequel vous voulez jouer (minimum 10, maximum 100) : "))
while nombres_allumettes < 10 or nombres_allumettes > 100:
    nombres_allumettes = int(input("Le nombre d'allumettes doit être entre 10 et 100. Donnez un nombre d'allumettes valide : "))

tour = 0
while nombres_allumettes > 0:
    if tour % 2 == 0:
        print(f"Il reste {nombres_allumettes} allumettes.")
        allumettes_jouees = int(input(f"C'est au tour de {joueur}. Combien d'allumettes voulez-vous prendre (1, 2 ou 3) ? "))
        while allumettes_jouees < 1 or allumettes_jouees > 3 or allumettes_jouees > nombres_allumettes:
            allumettes_jouees = int(input(f"Vous ne pouvez prendre que 1, 2 ou 3 allumettes, et pas plus que le nombre restant. Combien d'allumettes voulez-vous prendre ? "))
        nombres_allumettes -= allumettes_jouees
        if nombres_allumettes <= 0:
            print(f"{joueur} a pris la dernière allumette et perd la partie. {cpu} gagne !")
            break
    else:
        print(f"Il reste {nombres_allumettes} allumettes.")
        if nombres_allumettes % 4 == 0:
            allumettes_jouees = 3
        elif nombres_allumettes % 4 == 3:
            allumettes_jouees = 2
        elif nombres_allumettes % 4 == 2:
            allumettes_jouees = 1
        else:
            allumettes_jouees = 1
        print(f"C'est au tour de {cpu}. {cpu} prend {allumettes_jouees} allumette(s).")
        nombres_allumettes -= allumettes_jouees
        if nombres_allumettes <= 0:
            print(f"{cpu} a pris la dernière allumette et perd la partie. {joueur} gagne !")
            break
    tour += 1
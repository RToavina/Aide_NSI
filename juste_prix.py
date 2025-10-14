from random import randint
import random

# Version avec saisie du nombre à deviner par un joueur
# nombre_a_deviner = int(input("Choisissez un nombre entre 1 et 100 : "))
# while nombre_a_deviner < 1 or nombre_a_deviner > 100:
#     nombre_a_deviner = int(input("Le nombre doit être entre 1 et 100. Choisissez un nombre entre 1 et 100 : "))

# Version avec génération aléatoire du nombre à deviner
nombre_a_deviner = random.randint(1, 100)

nombres_essais = 0
nombre_parties_gagnées = 0

code_triche = 777

while 1:

    while nombres_essais < 10:
        nombre_saisi = int(input(f"Vous avez {10 - nombres_essais} essais pour deviner le juste prix : "))
        if nombre_saisi == code_triche:
            print(f"Le nombre à deviner est {nombre_a_deviner}")
        elif nombre_saisi<nombre_a_deviner:
            print("C'est plus")
            nombres_essais += 1
        elif nombre_saisi>nombre_a_deviner:
            print("C'est moins")
            nombres_essais += 1
        else:
            print(f"Gagné en {10-nombres_essais} coups")
            nombre_parties_gagnées += 1
            print("Voulez vous rejouer ? (o/n)")
            reponse = input().strip().lower()
            if reponse == "o":
                nombres_essais = 0
                nombre_a_deviner = random.randint(1, 100)
            else:
                print(f"Vous avez gagné {nombre_parties_gagnées} parties.")
                print("Merci d'avoir joué !")
                break
            
    print("Voulez vous rejouer ? (o/n)")
    reponse = input().strip().lower()
    if reponse == "o":
        nombres_essais = 0
        nombre_a_deviner = random.randint(1, 100)
    else:
        print(f"Vous avez gagné {nombre_parties_gagnées} parties.")
        print("Merci d'avoir joué !")
        break


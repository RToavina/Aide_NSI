## Jeu de la vie – NSI
# Auteur : Razanajatovo A. Toavina

# Le Jeu de la Vie est un automate cellulaire inventé par le mathématicien John Horton Conway en 1970.
# C'est un jeu de simulation dans lequel des cellules sur une grille évoluent selon des règles
# simples basées sur le nombre de voisins vivants. Chaque cellule peut être vivante (1) ou morte (0).
import random
import tkinter as tk

# PARTIE LOGIQUE DU JEU DE LA VIE
def afficher(tableau):
    """
    Affiche le tableau de manière lisible.
    """
    for ligne in tableau:
        print(ligne)

def nombre_voisins_vivants(i, j, tab):
    """
    Calcule le nombre de voisins vivants autour de la cellule (i, j).
    """
    voisins = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),          (0, 1),
               (1, -1), (1, 0), (1, 1)]
    nombre_voisins = 0
    for di, dy in voisins:
        ni, ny = i + di, j + dy
        if 0 <= ni < len(tab) and 0 <= ny < len(tab[0]):
            nombre_voisins += tab[ni][ny]
    return nombre_voisins


def voir_voisins(tableau):
    """
    Affiche le nombre de voisins vivants pour chaque cellule sous forme de matrice.
    """
    voisins_tableau = []
    for i in range(len(tableau)):
        ligne_voisins = []
        for j in range(len(tableau[0])):
            nb_voisins = nombre_voisins_vivants(i, j, tableau)
            ligne_voisins.append(nb_voisins)
        voisins_tableau.append(ligne_voisins)
    afficher(voisins_tableau)

def evolution(tab):
    """
    Calcule la prochaine génération du tableau selon les règles du Jeu de la Vie.
    """
    nouveau_tableau = []
    for i in range(len(tab)):
        nouvelle_ligne = []
        for j in range(len(tab[0])):
            nb_voisins = nombre_voisins_vivants(i, j, tab)
            if tab[i][j] == 1:
                if nb_voisins < 2 or nb_voisins > 3:
                    nouvelle_ligne.append(0)  # Meurt
                else:
                    nouvelle_ligne.append(1)  # Vit
            else:
                if nb_voisins == 3:
                    nouvelle_ligne.append(1)  # Naît
                else:
                    nouvelle_ligne.append(0)  # Reste morte
        nouveau_tableau.append(nouvelle_ligne)
    return nouveau_tableau

# PARTIE TKINTER
def dessiner_tableau(canvas, tableau, cellule_taille):
    """
    Docstring for dessiner_tableau
    
    :param canvas: la grille à afficher sur l'interfaece graphique
    :param tableau: le tableau de données à afficher
    :param cellule_taille: la taille de chaque cellule en pixels
    """
    canvas.delete("all")

    for i, ligne in enumerate(tableau):
        for j, cellule in enumerate(ligne):
            couleur = "black" if cellule == 1 else "white"
            canvas.create_rectangle(
                j * cellule_taille, i * cellule_taille,
                (j + 1) * cellule_taille, (i + 1) * cellule_taille,
                fill=couleur, outline="gray"
            )


def on_click(event, tableau, canvas, cellule_taille):
    """
    Docstring for on_click
    
    :param event: L'événement de clic de la souris
    :param tableau: Le tableau de données à modifier
    :param canvas: La grille sur laquelle le clic a été effectué
    :param cellule_taille: La taille de chaque cellule en pixels
    """
    x = event.y // cellule_taille
    y = event.x // cellule_taille

    if 0 <= x < len(tableau) and 0 <= y < len(tableau[0]):
        tableau[x][y] = 1 - tableau[x][y]
        dessiner_tableau(canvas, tableau, cellule_taille)

def lancer_pause():
    """
    Docstring for lancer_pause
    Lance ou met en pause l'animation du jeu de la vie.
    """
    global en_cours
    en_cours = not en_cours
    bouton_lancer.config(text="⏸ Pause" if en_cours else "▶ Lancer")
    if en_cours:
        boucle_animation()

def prochaine_generation():
    """
    Docstring for prochaine_generation
    Calcule et affiche la prochaine génération du tableau.
    """
    global tableau
    tableau = evolution(tableau)
    dessiner_tableau(canvas, tableau, CELLULE_TAILLE)

def boucle_animation():
    """
    Docstring for boucle_animation
    Gère la boucle d'animation en appelant la fonction de génération suivante à intervalles réguliers.
    """
    if en_cours and animation_auto:
        prochaine_generation()
        fenetre.after(VITESSE, boucle_animation)

def toggle_animation():
    """
    Docstring for toggle_animation
    Active ou désactive l'animation automatique du jeu de la vie.
    """
    global animation_auto
    animation_auto = not animation_auto
    bouton_animation.config(
        text="🔁 Animation ON" if animation_auto else "🔁 Animation OFF"
    )
    if en_cours and animation_auto:
        boucle_animation()

def toggle_mode():
    """
    Docstring for toggle_mode
    Met en pause le jeu et bascule entre le mode édition et le mode simulation.
    """
    global mode_edition
    mode_edition = not mode_edition
    bouton_mode.config(
        text="✏ Mode édition" if mode_edition else "🎮 Mode simulation"
    )

def reinitialiser():
    """
    Docstring for reinitialiser
    Reinitialise le tableau à un état vide et met en pause le jeu.
    """
    global tableau, en_cours

    en_cours = False
    bouton_lancer.config(text="▶ Lancer")

    tableau = [
        [0 for _ in range(n_colonnes)]
        for _ in range(n_lignes)
    ]

    dessiner_tableau(canvas, tableau, CELLULE_TAILLE)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PROGRAMME PRINCIPAL
if __name__ == "__main__":
   
   #PARAMÈTRES
    CELLULE_TAILLE = 40
    VITESSE = 500  # ms
    n_lignes = int(input("Saisir le nombre de lignes: "))
    n_colonnes = int(input("Saisir le nombre de colonnes: "))
    
    # Initialisation aléatoire du tableau
    tableau = [[random.randint(0, 1) for _ in range(n_colonnes)] for _ in range(n_lignes)]

    #Etat de notre jeu
    en_cours = False
    mode_edition = True
    animation_auto = False   

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# INTERFACE GRAPHIQUE
    fenetre = tk.Tk()
fenetre.title("Jeu de la vie – NSI")

canvas = tk.Canvas(
    fenetre,
    width=n_colonnes * CELLULE_TAILLE,
    height=n_lignes * CELLULE_TAILLE
)
canvas.pack()
canvas.bind(
    "<Button-1>",
    lambda event: on_click(event, tableau, canvas, CELLULE_TAILLE)
)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# BOUTONS
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Frame pour les boutons
frame_boutons = tk.Frame(fenetre)
frame_boutons.pack(pady=5)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bouton_lancer = tk.Button(frame_boutons, text="▶️ Lancer", command=lancer_pause)
bouton_lancer.grid(row=0, column=0, padx=5)

bouton_gen = tk.Button(frame_boutons, text="⏭️ Génération suivante", command=prochaine_generation)
bouton_gen.grid(row=0, column=1, padx=5)

bouton_animation = tk.Button(frame_boutons, text="🔁 Animation OFF", command=toggle_animation)
bouton_animation.grid(row=0, column=2, padx=5)

bouton_mode = tk.Button(frame_boutons, text="🔨 Mode édition", command=toggle_mode)
bouton_mode.grid(row=0, column=3, padx=5)

bouton_reset = tk.Button(frame_boutons,text="🔄 Réinitialiser",command=reinitialiser)
bouton_reset.grid(row=0, column=4, padx=5)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
dessiner_tableau(canvas, tableau, CELLULE_TAILLE)
fenetre.mainloop()
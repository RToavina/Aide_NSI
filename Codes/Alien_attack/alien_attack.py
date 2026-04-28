import pyxel
import random

pyxel.init(128, 128, title="Alien Attack")

# Variables globales - Etape 1
carre_x = 60
carre_y = 110

# Variables globales - Etape 2
tirs_liste = []

# Variables globales - Etape 3
ennemis_liste = []

# Variables globales - Etape 4b
vies = 3

# Score
score = 0

# Etoiles en fond (position x, y, couleur)
etoiles = [[random.randint(0, 127), random.randint(0, 127), random.choice([1, 2, 6, 13])] for _ in range(40)]


# Dessin du vaisseau rouge (forme de vaisseau en pixel art)
def dessiner_vaisseau(x, y):
    # Corps principal
    pyxel.rect(x + 3, y, 2, 2, 8)       # pointe
    pyxel.rect(x + 2, y + 2, 4, 2, 8)   # milieu
    pyxel.rect(x, y + 4, 8, 3, 8)        # base
    # Ailes
    pyxel.pset(x, y + 5, 14)
    pyxel.pset(x + 7, y + 5, 14)
    # Moteur
    pyxel.rect(x + 1, y + 7, 2, 1, 9)
    pyxel.rect(x + 5, y + 7, 2, 1, 9)


# Dessin d'un ennemi alien (forme simple pixel art)
def dessiner_ennemi(x, y):
    # Corps
    pyxel.rect(x + 2, y, 4, 2, 11)
    pyxel.rect(x + 1, y + 2, 6, 3, 11)
    pyxel.rect(x, y + 5, 8, 2, 11)
    # Yeux
    pyxel.pset(x + 2, y + 3, 0)
    pyxel.pset(x + 5, y + 3, 0)
    # Pattes
    pyxel.pset(x + 1, y + 7, 11)
    pyxel.pset(x + 3, y + 7, 11)
    pyxel.pset(x + 4, y + 7, 11)
    pyxel.pset(x + 6, y + 7, 11)


# Etape 1 - Deplacement du carre
def carre_deplacement(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT):
        x = x - 2
    if pyxel.btn(pyxel.KEY_UP):
        y = y - 2
    if pyxel.btn(pyxel.KEY_DOWN):
        y = y + 2
    if x < 0:
        x = 0
    if x > 120:
        x = 120
    if y < 0:
        y = 0
    if y > 120:
        y = 120
    return x, y


# Etape 2 - Creation des tirs
def tirs_creation(x, y, tirs_liste):
    # btnr pour eviter les tirs multiples
    if pyxel.btnr(pyxel.KEY_SPACE):
        # Les tirs partent du centre du vaisseau
        tirs_liste.append([x + 4, y])
    return tirs_liste


# Etape 2 - Deplacement des tirs
def tirs_deplacement(tirs_liste):
    for tir in tirs_liste[:]:
        # Les tirs se deplacent du bas vers le haut
        tir[1] -= 3
        if tir[1] < -8:
            tirs_liste.remove(tir)
    return tirs_liste


# Etape 3 - Creation des ennemis
def ennemis_creation(ennemis_liste):
    # Un ennemi arrive toutes les 30 frames soit 1 seconde
    if pyxel.frame_count % 30 == 0:
        ennemis_liste.append([random.randint(0, 120), 0])
    return ennemis_liste


# Etape 3 - Deplacement des ennemis
def ennemis_deplacement(ennemis_liste):
    for ennemi in ennemis_liste[:]:
        ennemi[1] += 1
        if ennemi[1] > 120:
            ennemis_liste.remove(ennemi)
    return ennemis_liste


# Etape 4a - Suppression des ennemis touches par un tir
def ennemis_suppression():
    # Fonctionne par effet de bord : modifie directement tirs_liste
    # et ennemis_liste sans les retourner, car ce sont des listes
    # (objets mutables Python passes par reference).
    global score
    for ennemi in ennemis_liste[:]:
        for tir in tirs_liste[:]:
            if (ennemi[0] <= tir[0] + 1 and
                    ennemi[0] + 8 >= tir[0] and
                    ennemi[1] + 8 >= tir[1]):
                if ennemi in ennemis_liste:
                    ennemis_liste.remove(ennemi)
                if tir in tirs_liste:
                    tirs_liste.remove(tir)
                score += 10
                break


# Etape 4b - Collision entre les ennemis et le vaisseau
def vaisseau_suppression(vies):
    for ennemi in ennemis_liste[:]:
        if (ennemi[0] <= carre_x + 8 and
                ennemi[1] <= carre_y + 8 and
                ennemi[0] + 8 >= carre_x and
                ennemi[1] + 8 >= carre_y):
            ennemis_liste.remove(ennemi)
            vies -= 1
    return vies


def update():
    global carre_x, carre_y, tirs_liste, ennemis_liste, vies

    if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()

    if vies > 0:
        carre_x, carre_y = carre_deplacement(carre_x, carre_y)

        tirs_liste = tirs_creation(carre_x, carre_y, tirs_liste)
        tirs_liste = tirs_deplacement(tirs_liste)

        ennemis_liste = ennemis_creation(ennemis_liste)
        ennemis_liste = ennemis_deplacement(ennemis_liste)

        ennemis_suppression()

        vies = vaisseau_suppression(vies)


def draw():
    pyxel.cls(0)

    # Fond etoile
    for etoile in etoiles:
        pyxel.pset(etoile[0], etoile[1], etoile[2])

    # Affichage vies et score
    pyxel.text(2, 2, 'VIES:' + str(vies), 7)
    pyxel.text(70, 2, 'SCORE:' + str(score), 10)

    if vies > 0:
        # Vaisseau
        dessiner_vaisseau(carre_x, carre_y)

        # Tirs
        for tir in tirs_liste:
            pyxel.rect(tir[0], tir[1], 1, 4, 10)
            pyxel.pset(tir[0], tir[1], 7)

        # Ennemis
        for ennemi in ennemis_liste:
            dessiner_ennemi(ennemi[0], ennemi[1])

    else:
        # Game Over au centre de l'ecran
        pyxel.rect(24, 50, 80, 30, 0)
        pyxel.rectb(24, 50, 80, 30, 8)
        pyxel.text(40, 57, 'GAME OVER', 8)
        pyxel.text(28, 67, 'SCORE: ' + str(score), 7)
        pyxel.text(27, 75, 'Q pour quitter', 13)


pyxel.run(update, draw)

import pyxel
import random
import math

pyxel.init(128, 128, title = 'Tower_defense', )
pyxel.load ('U2.pyxres')
vitesse = 0.5
vitesse_balle = 5
ennemis_liste = []
tirs_liste = []
explosions_liste = [] 
minutes = 0
secondes = 0
vie = 3
score = 0

def update():
    global ennemis_liste, tirs_liste, explosions_liste, minutes, secondes, score
    if vie <= 0:
        return
    
    ennemis_liste = ennemis_creation(ennemis_liste)
    ennemis_liste = ennemis_deplacement(ennemis_liste)
    tirs_liste = tir_creation(tirs_liste)
    tirs_liste = tir_deplacement(tirs_liste)
    
    explosions_liste, score = explosion_tirs(tirs_liste, ennemis_liste, explosions_liste, score)
    
    minutes, secondes = timing()

    
def draw():
    global vie, score
    if vie <= 0:
        pyxel.cls(0)
        pyxel.text(47, 54, "GAME OVER", 4)
        pyxel.text(47, 62, f"{minutes}:{secondes}", 4)
        pyxel.text(47, 68, f"score:{score}", 4)
    else:
        pyxel.cls(0)
        pyxel.blt(54, 50, 0, 0, 128, 15, 15, 4, 0, 2)
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 48, 160, 15, 15, 4, 0, 0.5)
        pyxel.blt(47, 27, 0, 0, 64, 31, 23, 4, 0, 0.5)
        
        for i in range(len(ennemis_liste) - 1, -1, -1):
            pyxel.blt(ennemis_liste[i][0], ennemis_liste[i][1], 0, 8, 96, 15, 15, 4, 0, 0.5)
            if abs(ennemis_liste[i][0] - 54) < 10 and abs(ennemis_liste[i][1] - 50) < 15:
                pyxel.blt(ennemis_liste[i][0], ennemis_liste[i][1], 0, 80, 144, 15, 15, 4, 0, 0.5)
                ennemis_liste.pop(i)
                vie -= 1
                
        for t in tirs_liste:
            pyxel.blt(t[0], t[1], 0, 0, 144, 15, 15, 4, 0, 0.5)
    
        for exp in explosions_liste:
            pyxel.blt(exp[0], exp[1], 0, 64, 144, 15, 15, 4, 0, 0.5)
            
        pyxel.text(0, 120, f"{minutes}:{secondes}", 7)
        
        pyxel.text(100, 120, f"score:{score}", 7)
        stats()


            
def tir_deplacement(liste_actuelle):
    for t in liste_actuelle:
        t[0] += t[2]
        t[1] += t[3]
    for i in range(len(liste_actuelle) - 1, -1, -1):
         if liste_actuelle[i][0] < -15 or liste_actuelle[i][0] > 143 or liste_actuelle[i][1] < -15 or liste_actuelle[i][1] > 143:
             liste_actuelle.pop(i)
    return liste_actuelle


def tir_creation(liste_actuelle):
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        cible_x = pyxel.mouse_x
        cible_y = pyxel.mouse_y
        
        depart_x = 47
        depart_y = 27
        
        dx = cible_x - depart_x
        dy = cible_y - depart_y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance != 0:
            vx = (dx / distance) * vitesse_balle
            vy = (dy / distance) * vitesse_balle
            liste_actuelle.append([depart_x, depart_y, vx, vy])
    return liste_actuelle
    
def ennemis_creation(liste_actuelle):
    if pyxel.frame_count % 30 == 0:
        liste_actuelle.append([random.randint (-64, 128), random.randint (-64, 128)])
    return liste_actuelle
    
def ennemis_deplacement(liste_actuelle):
    for y in liste_actuelle:
        if y[0] < 54:
            y[0] += vitesse
        elif y[0] > 54:
            y[0] -= vitesse
    
        if y[1] < 50:
            y[1] += vitesse
        elif y[1] > 50:
            y[1] -= vitesse
    return liste_actuelle

def explosion_tirs(liste_actuelle_tirs, liste_actuelle_ennemis, liste_actuelle_explosions, score):
    for t_ex in range(len(liste_actuelle_tirs) - 1, -1, -1):
        for i_ex in range(len(liste_actuelle_ennemis) - 1, -1, -1):
            if abs(liste_actuelle_tirs[t_ex][0] - liste_actuelle_ennemis[i_ex][0]) < 8 and abs(liste_actuelle_tirs[t_ex][1] - liste_actuelle_ennemis[i_ex][1]) < 8:

                liste_actuelle_explosions.append([liste_actuelle_tirs[t_ex][0], liste_actuelle_tirs[t_ex][1], 10])
                
                liste_actuelle_tirs.pop(t_ex)
                liste_actuelle_ennemis.pop(i_ex)
                score += 1 
                break 
            
    for e in range(len(liste_actuelle_explosions) - 1, -1, -1):
        liste_actuelle_explosions[e][2] -= 1 
        if liste_actuelle_explosions[e][2] <= 0:
            liste_actuelle_explosions.pop(e)
            
    return liste_actuelle_explosions, score
    
def timing():
    totale_s = pyxel.frame_count // 30
    m = totale_s // 60
    s = totale_s - m*60
    return m,s
    
def stats():
    for i in range(3):
        x_coeur = 112 - (i * 12)
        y_coeur = 4
        if i < vie:
            pyxel.blt(x_coeur, y_coeur, 0, 80, 160, 15, 15, 4)
        else:
            pyxel.blt(x_coeur, y_coeur, 0, 112, 160, 15, 15, 4)
            
pyxel.run(update, draw)
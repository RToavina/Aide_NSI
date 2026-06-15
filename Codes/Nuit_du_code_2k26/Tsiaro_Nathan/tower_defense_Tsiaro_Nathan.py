# Pyxel Studio
import pyxel
import random
pyxel.init(250,250,title='toward defense', fps=40)

pyxel.load('U2.pyxres')
x = 125
y = 125
tirs_liste = []
temps = 0
nbr_vague=24
enn_list=[]
explo = []
vie = 6
collision=[]

def troupe_deplacement(x,y):
    if pyxel.btn(pyxel.KEY_RIGHT) and x < 221 :
        x = x + 2
    if pyxel.btn(pyxel.KEY_LEFT) and 0 < x :
        x = x - 2
    if pyxel.btn(pyxel.KEY_UP) and y > 0:
        y = y - 2
    if pyxel.btn(pyxel.KEY_DOWN) and y < 221:
        y = y + 2
    return x,y
   
def tir_creation(x,y,tirs_liste):
    global temps
    if pyxel.btn(pyxel.KEY_SPACE) and temps == 0:
        tirs_liste.append([x+5,y-3])
        temps = 20
    return tirs_liste
   
def tir_deplacement(tirs_liste):
    for tir in tirs_liste:
        tir[1] -= 1
        if tir[1]<0:
            tirs_liste.remove(tir)
    return tirs_liste

   
def creation_ennemies(enn_list):
    if pyxel.frame_count % 30 ==0:
        enn_list.append([random.randint(0,231),0])
    return enn_list
   
def ennemie_deplacement(enn_list):
    global vie
    for ennemie in enn_list:
        ennemie[1]+=1
        if ennemie[1]>207:
            collision.append([ennemie[0], ennemie[1], 10])

            vie = vie -1
            enn_list.remove(ennemie)
    return enn_list

def ennemie_suppression():
    for enemi in enn_list:
        for tir in tirs_liste:
            if tir[0] < enemi[0] + 31 and tir[0] + 5 > enemi[0] and tir[1] < enemi[1] + 23 and tir[1] + 13 > enemi[1]:
                explo.append([enemi[0], enemi[1], 10])
                if enemi in enn_list:
                    enn_list.remove(enemi)
                if tir in tirs_liste:
                    tirs_liste.remove(tir)

def dure(liste):
    for e in liste[:]:
        e[2] -= 1
        if e[2] <= 0:
            liste.remove(e)
           
def ennemies_suppression_1():

    global vie
    for ennemie in enn_list:
        if ennemie[1]==207:

            vie = vie -1
            if ennemie in enn_list:
                enn_list.remove(ennemie)

def update():
    global x, y, tirs_liste, temps, enn_list, explo, vie, collision, nbr_vague
    if temps > 0 :
        temps = temps - 1
    if vie == 0:
        if pyxel.btn(pyxel.KEY_R):

            x = 125
            y = 125
            tirs_liste = []
            temps = 0
            nbr_vague=24
            enn_list=[]
            explo = []
            vie = 6
            collision=[]
        return
    x, y =  troupe_deplacement(x,y)
    tirs_liste = tir_creation (x,y,tirs_liste)
    tirs_liste = tir_deplacement(tirs_liste)
    enn_list=creation_ennemies(enn_list)
    enn_list=ennemie_deplacement(enn_list)
    ennemie_suppression()
    dure(explo)
    dure(collision)
   
def draw():
    pyxel.cls(0)
    if vie > 0:

        for a in range(0,250,5):
            for b in range(230,250,5):
                pyxel.blt(a,b,0,121,136,5,5)
        for tir in tirs_liste:
            pyxel.blt(tir[0], tir[1], 0, 17, 128, 5, 13, 4)

        for ennemie in enn_list:
            pyxel.blt(ennemie[0],ennemie[1],0,0,0,31,-23,4)
        for expl in explo:
            pyxel.blt(expl[0], expl[1], 0, 64, 144, 15, 15, 4)

        for k in collision:
            pyxel.blt(k[0],k[1],0,65,129,13,13,4)
            pyxel.blt(k[0],k[1],0,80,128,15,15,4)
        for i in range(6):
            if i < vie:
                pyxel.blt(i * 15 + 5, 5, 0, 80 , 160, 13, 11, 4)
            else:
                pyxel.blt(i * 15 + 5, 5, 0, 112, 160, 13, 11, 4)
        pyxel.blt(x, y, 0, 8, 100, 19, 10, 4)
       
    else:
        pyxel.text(125,125,"GAME OVER", 7)
        pyxel.text(130,130,"PRESS R TO RESTART", 7)
   
   
       
   
   
   
pyxel.run(update, draw)
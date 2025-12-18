from random import randint

def crea_jeu ( ) :
    """
    Déroulement de la partie

    - On dispose d'un jeu de 24 cartes de couleur vertes, violettes ou orange sur lesquelles est porté un nombre.
    - Distribuer aléatoirement 12 cartes à chaque joueur.
    - Simultanément chaque joueur joue une carte, la carte la plus forte emporte le le pli. Le jeu se joue donc en 12 plis.
    - Quand toutes les cartes sont jouées, chaque joueur fait la somme des nombres portés par les cartes, le plus fort total l'emporte.
    
    Retourne le jeu de cartes sous forme d'une liste de tuples (couleur, valeur)
    où couleur est un entier (0 pour violet, 1 pour vert, 2 pour orange)
    et valeur est un entier représentant la valeur de la carte.
    
    Valeur des cartes

    - Les cartes oranges l'emportent sur les cartes vertes et violettes.
    - Les cartes vertes l'emportent sur les cartes violettes.
    - Si deux cartes violettes sont jouées en même temps la plus grande l'emporte.
    - Si deux cartes vertes sont jouées en même temps la plus grande l'emporte
    - Si deux cartes identiques sont jouées en même temps, les cartes sont écartées et ne compteront pas dans le total final.

    """
    jeu = []
    oranges = [0 for i in range(4)]
    vertes = [i for i in range(1, 11)]
    violettes = [ i*10 for i in vertes if i%2 != 0]
    violettes = violettes * 2
    for i in vertes :
        jeu.append((1, i))
    for i in violettes :
        jeu.append((0, i))
    for i in oranges :
        jeu.append((2, i))
    return jeu

jeu = crea_jeu( )

def distribue(jeu) :
    """
    Le jeu de cartes est distribué aléatoirement entre les deux joueurs. On constitue ainsi deux jeux de cartes qui sont les listes jeu1 et jeu2 qui correspondent aux jeux de chacun des joueurs.
    La fonction distribue(jeu) renvoie un tuple contenant les deux listes jeu1 pour le joueur 1 et jeu2 pour le joueur 2 :
    """
    jeu1 , jeu2 = [], []
    while len(jeu) != 0 :
        a = randint(0, len (jeu) - 1)
        jeu1.append(jeu[a])
        del jeu[a]
        b = randint(0, len(jeu) - 1 )
        jeu2.append(jeu[b])
        del jeu[b]
    return jeu1, jeu2

distribue(jeu)

def pli (carte1, carte2) :
    """ carte1 et carte2 : tuples de la forme (Couleur, Valeur) """
    """ retourne un tuple : carte ayant remporte le pli """
    """ retourne None en cas d'egalite """

    # On compare les cartes selon les regles du jeu
    if (carte1[0] == 2 and carte2[0] != 2) or (carte1[0] == 1 and carte2[0]==0) :
        return carte1
    # On compare les cartes selon les regles du jeu
    elif (carte2[0] == 2 and carte1[0] != 2) or (carte2[0] == 1 and carte1[0]==0) :
        return carte2
    # Cas ou les cartes sont de meme couleur
    else :
        if carte1[1] > carte2[1] :
            return carte1
        elif carte2[1] > carte1[1] :
            return carte2
    # Cas d'egalite
    return None

def jouer_carte1(main) :
    """ main : la liste non vide de cartes représentant le jeu de la petite nièce 
    la fonction retourne la carte jouée """
    return main[0]

def jouer_carte2(main) :
    """ main est une liste de cartes que peut jouer le programme
    la fonction retourne la carte jouée"""
    liste1 = [i[1] for i in main if i[0]==1]
    liste2 = [i[1] for i in main if i[0]==0]
    for i in main:
        if i[0] == 2 :
            return i
    for i in main:
        if i[0] == 1 and i[1] == max(liste1) :
            return i
    for i in main:
        if i[1] == min(liste2):
            return i
    return main[0]

def JouerUneCarte(ListeCartes1, ListeCartes2):
    """
    
    Fonction qui choisi la carte qu'il faut jouer en fonction de la main du joueur 1 et du joueur 2.
    L'objectif est de battre le robot à tous les coups en sachant que la partie se joue en 1000 donnes.
    On peut même aller plus loin car on connait le jeu de l'adversaire on peut choisir 
    la carte à jouer en fonction du jeu de l'adversaire.

    params:
    ListeCartes1 : liste de vos cartes de la forme [couleur, valeur]
    ListeCartes2 : liste des cartes de l'adversaire de la forme [couleur, valeur]

    """

    liste1 = [i[1] for i in ListeCartes1 if i[0]==1]
    liste2 = [i[1] for i in ListeCartes1 if i[0]==0]

    # On joue la carte la plus forte possible pour battre l'adversaire
    for i in range(len(ListeCartes1)) :
        if ListeCartes1[i][0] == 2 :
            carte = ListeCartes1[i]
            return carte
    
    # On joue la carte verte la plus forte possible
    for i in range(len(ListeCartes1)) :
        if ListeCartes1[i][0] == 1 and ListeCartes1[i][1] == max(liste1) :
            carte = ListeCartes1[i]
            return carte
    
    # On joue la carte violette la plus faible possible
    for i in range(len(ListeCartes1)) :
        if ListeCartes1[i][0] == 0 and ListeCartes1[i][1] == min(liste2) :
            carte = ListeCartes1[i]
            return carte
    
    # Si aucune carte ne peut être jouée pour battre l'adversaire, on joue la première carte
    carte = ListeCartes1[0]
    return carte

#la partie, renvoie le gagnant.
def partie():
    joueur1, joueur2 = distribue(crea_jeu())
    score1, score2 = 0, 0
    for i in range(12):
        cartej1 = jouer_carte1(joueur1)
        joueur1.remove(cartej1)
        cartej2 = jouer_carte2(joueur2)
        joueur2.remove(cartej2)
        gagnant = pli(cartej1, cartej2)
        if gagnant == cartej1:
            score1 += cartej1[1] + cartej2[1]
        elif gagnant == cartej2:
            score2 += cartej1[1] + cartej2[1]
    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 0

# Programme principal, on joue 1000 parties
g1, g2 = 0, 0
for x in range(1000):
    r = partie()
    if r == 1:
        g1 += 1
    if r == 2:
        g2 += 1
print("Joueur 1 =", g1, "Joueur 2 =", g2)










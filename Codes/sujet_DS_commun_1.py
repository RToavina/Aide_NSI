#Exo 1

print("Exo 1 \n")
#Question 1
x = 5
y = 7
for i in range(y):
    x = x + 1

print("Question 1 : x = ",x)

#Question 2
#x = 4
#while x>0:
#    y = 1
#    while y<x:
#        x = x - 1
#        y = y + 1

print("Question 2 : Boucle infinie")

#Question 3
def mystere(n):
    a = 1
    for i in range(n):
        a = a * 2
    return a

print("Question 3 : mystere(4) = ",mystere(4))

#Question 4
def puissance(x,y):
    p = x
    for i in range(y):
        p = p * x
    return p

#assert puissance(0,1) == 0
#assert puissance(1,1) == 1
#assert puissance(1,0) == 1
print("Question 4 : assert puissance(2,1) == 2")


#Question 5
def addition(a,b):
    p = a + b
    return p

#addition(1,2)
#addition("a","b")
print("Question 5 : addition('a',2)")
#addition(1,2.0)

#Question 6
def mystere(a):
    """Renvoie True si a est divisible par 3, sinon False"""
    return a%3==0

#Exo 2

print("Exo 2\n")
#Question 1
def compte_mots(a):
    cpt  = 0
    for i in a:
        if i == ' ' or i == '.':
            cpt = cpt + 1
    return cpt 

print("Question 1 : Exemple de prototype pour compte_mots : compte_mots('Bonjour le monde.') =",compte_mots('Bonjour le monde.'))

#Question 2
print("Question 2 : ",compte_mots("Bonjour le monde."))  # Doit renvoyer 2

#Question 3
print("Question 3 : La précondition est que la chaîne de caractères se termine par un espace ou un point.")

#Qestion 4
def compte_mots_v2(a):
    cpt  = 0
    for i in a:
        if i == ' ' and  i == '.':
            cpt = cpt + 1
    return cpt

print("Question 4 : Exemple de ce que retournera cette fonction pour compte_mots_v2('Bonjour le monde.') =",compte_mots_v2('Bonjour le monde.'))

#Question 5

print(
"""
Question 5 : 
def compte_mots_v3(a):
    cpt  = 0
    for i in range(len(a)):
        if a[i] == ' ' or (a[i] == '.' and i == len(a)-1):
            cpt = cpt + 1
    return cpt
"""
)

#Exo 3
print("Exo 3")
#Partie A Filtrage
print("Partie A Filtrage")
print("""
def filtrer_liste(liste,seuil):
    nouvelle_liste = []
    for element in liste:
        if element >= seuil:
            nouvelle_liste.append(element)
    return nouvelle_liste
""")

#Partie B Modification "In Place"
print("Partie B Modification In Place")
print("""
def zeros_a_la_fin(L):
    ""Prend en argument une liste d'entiers L. Cette fonction doit modifier la liste L sur place(in-place),
    sans en créer une nouvelle, de telle sorte que tous les zéros de L soient déplacés à la fin de la liste,
    ""

    n = len(L)
    i = 0
    while i < n:
        if L[i] == 0:
            L.append(L.pop(i))
            n -= 1
        else:
            i += 1
    return L
""")

#Exo 4
print("Exo 4")

print("Algorithme de fusion de deux listes")

print("""
def fusionner(L1,L2):
    ""Prend en arguments deux listes triées L1 et L2 et renvoie une nouvelle liste triée contenant tous les éléments de L1 et L2.
    Contrainte : La fonction doit parcourir une seule fois chaque liste.
    ""
    L3 = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L3.append(L1[i])
            i += 1
        else:
            L3.append(L2[j])
            j += 1
    while i < len(L1):
        L3.append(L1[i])
        i += 1
    while j < len(L2):
        L3.append(L2[j])
        j += 1
    return L3
""")






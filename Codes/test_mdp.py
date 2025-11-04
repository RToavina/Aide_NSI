def test_mdp(chaine:str) -> bool:
    #Liste des minuscules
    minuscule = 'qwertyuiopasdfghjklzxcvbnm'
    bool_min = False
    
    #Liste des majuscules
    majuscule = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    bool_maj = False
    
    #Liste des caracteres speciaux
    speciale = '%$*#?!£µ&@'
    bool_s = False
    
    #Liste des chiffres
    chiffre = '1234567890'
    bool_c = False
    
    #EQUIVALENT BOUCLE WHILE
    #i = 0
    
    longueur_mot = len(chaine)
    
    mdp_OK = False
    
    if longueur_mot < 8:
        return False
    
    #EQUIVALENT BOUCLE FOR
    for caractere in chaine:
        if caractere in minuscule:
            bool_min = True
        elif caractere in majuscule:
            bool_maj = True
        elif caractere in speciale:
            bool_s = True
        elif caractere in chiffre:
            bool_c = True

    #EQUIVALENT BOUCLE WHILE
    #while i<longueur_mot and not(mdp_OK):
    #    caractere_en_cours = chaine[i] 
    #    if caractere_en_cours in minuscule:
    #        bool_min = True
    #    elif caractere_en_cours in majuscule:
    #        bool_maj = True
    #    elif caractere_en_cours in speciale:
    #        bool_s = True
    #    elif caractere_en_cours in chiffre:
    #        bool_c = True
    #    i+=1
    #    mdp_OK = bool_min and bool_maj and bool_s and bool_c
    
    mdp_OK = bool_min and bool_maj and bool_s and bool_c
        
    return mdp_OK

print(test_mdp("1Zcet1$")) 
print(test_mdp("qwertyuiop"))
print(test_mdp("qwertyuiop12"))
print(test_mdp("QWERTYUIOP12@")) 
print(test_mdp("Qwerty@#")) 
print(test_mdp("Qwertyuiop12@")) 
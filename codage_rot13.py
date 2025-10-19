def codage_rot13(texte):
    """Applique le codage ROT13 à une chaîne de caractères."""
    resultat = []
    for caractere in texte: # Parcours de chaque caractère dans le texte
        if 'a' <= caractere <= 'z': # Vérifie si le caractère est une lettre minuscule
            decalage = (ord(caractere) - ord('a') + 13) % 26
            nouveau_caractere = chr(ord('a') + decalage)
            resultat.append(nouveau_caractere)
        elif 'A' <= caractere <= 'Z': # Vérifie si le caractère est une lettre majuscule
            decalage = (ord(caractere) - ord('A') + 13) % 26
            nouveau_caractere = chr(ord('A') + decalage)
            resultat.append(nouveau_caractere)
        else: # Si ce n'est pas une lettre, on le laisse inchangé
            resultat.append(caractere)
    return ''.join(resultat)

# Exemple d'utilisation
if __name__ == "__main__":
    texte = "Bonjour le Monde!"
    print(codage_rot13(texte))
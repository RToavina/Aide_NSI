def moyenne(tab):
    n = len(tab)
    if n == 0:
        return None  # Évite la division par zéro pour une liste vide
    somme = 0
    for note in tab:
        somme += note
    return somme / n


#exemple d'utilisation
notes = [12, 15, 14, 10, 18]

print("La moyenne est :", moyenne(notes))  # Devrait afficher La moyenne est : 13.8


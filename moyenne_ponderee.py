def moyenne_ponderee(notes, coefficients):
    n = len(notes)
    if n == 0 or n != len(coefficients):
        return None  # Évite la division par zéro ou les listes de tailles différentes
    somme_ponderee = 0
    somme_coefficients = 0
    for i in range(n):
        somme_ponderee += notes[i] * coefficients[i]
        somme_coefficients += coefficients[i]
    return somme_ponderee / somme_coefficients

# Exemple d'utilisation
notes = [12, 15, 14, 10, 18]    
coefficients = [2, 3, 1, 4, 2]

print("La moyenne pondérée est :", moyenne_ponderee(notes, coefficients))  # Devrait afficher La moyenne pondérée est : 13.88888888888889
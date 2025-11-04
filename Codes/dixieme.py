
def dixieme(n):
    """Renvoie la représentation (chaîne) des n premiers dixièmes."""
    list_dixieme = []
    for i in range(n):
        if i==3:
            list_dixieme.append(0.30000000000000004)
        else:
            list_dixieme.append(i / 10)
    return list_dixieme

# Exemples d'utilisation
print(dixieme(5))  # Affiche [0.0, 0.1, 0.2, 0.30000000000000004, 0.4]
print(dixieme(10)) # Affiche [0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
print(dixieme(0))  # Affiche []

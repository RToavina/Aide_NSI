def arrets(distancesStations, distancePlein):
    """
    distancesStations est la liste des distances entre les différentes stations
    [DS1, S1S2, ... , SNA]
    distancePlein est la distance parcourue par le camion avec un plein.
    renvoie la liste des stations où prendre de l'essence.

    >>> arrets([30,30,30,30,30,30,30,15] , 100)
    [3, 6]
    """

    reservoir = distancePlein
    resultat = []

    i = 0

    while(i<len(distancesStations)):
        reservoir -= distancesStations[i]
        
        if reservoir <= 0:
            reservoir = distancePlein
            resultat.append(i)
            i -= 1
        i+=1

    return resultat

print(arrets([30,30,30,30,30,30,30,15] , 100))
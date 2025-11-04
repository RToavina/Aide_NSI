def estPremier(n):
    if n < 2:
        return False
    
    #Equivalent boucle while
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1

    # #Equivalent boucle for
    # for i in range(2, n):
    #     if n % i == 0:
    #         return False
        
    return True

print(estPremier(1))  # False
print(estPremier(2))  # True
print(estPremier(13))  # True
print(estPremier(15))  # False
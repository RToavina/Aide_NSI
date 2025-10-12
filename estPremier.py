def estPremier(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(estPremier(1))  # False
print(estPremier(2))  # True
print(estPremier(13))  # True
print(estPremier(15))  # False
def somme(n):
    total = 0
    for i in range(n):
        if i%3==0 or i%5==0:
            total+=i
    return total

print(somme(10))
print(somme(1000))
print(somme(2))
print(somme(5))
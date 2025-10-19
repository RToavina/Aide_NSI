def javanais(text):
    vowels = "aeiouAEIOU"
    result = []
    for char in text:
        if char in vowels:
            result.append("av" + char)
        else:
            result.append(char)
    return ''.join(result)

# Exemple d'utilisation
if __name__ == "__main__":
    texte = "C'est fort"
    print(javanais(texte)) 
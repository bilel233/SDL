# ajouter deux nombres en python

# avec l'operateur "+"

a = 1
b = 2

s = a + b  # on somme les nombres



print(f" a = {a} et b = {b}")   # on affiche les valeurs

# ajouter deux nombres avec la fonction input

a = int(input("premier nombre")) # saisit des nombres
b = int(input("second nombre"))

s = a + b   # somme des nombres

print(f"s = {s}")   # affichage de la somme

# somme de deux nombres avec creation de fonction

def add(a,b):
    """renvoie la somme de deux nombres"""

    return a + b

# on teste la fonction

print(f"somme  = {add(10,11)}")



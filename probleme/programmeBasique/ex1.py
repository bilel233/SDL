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

# ajouter deux nombres en utilsant operator.add methode

from operator import add

num1 = 15
num2 = 12

# additioner les nombres

s = add(num1,num2)
print(f"la somme vaut {s}")

#utilisation de la methode lambda fonction

s = lambda x,y:x+y

print(f"la somme s vaut  {s(1,2)}")

# additionner deux nombres avec une fonction recursive

def add_numbers(x,y):
    """ renvoie la somme de deux nombres"""

    if y == 0:
        return x
    return add_numbers(x+1,y-1)

print(f"s = {add_numbers(2,3)}")
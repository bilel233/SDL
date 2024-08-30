# additionner deux nombres avec l'operateur +

a = 15
b = 12

sum = a + b     # on realise la somme des deux nombres

print(f"la somme des deux nombres vaut : {sum}")


# utilisation de l'operateur input

n1 = input("veuillez saisir un nombre") # saisit du premier nombre
n2 = input("veuillez saisir un nombre") # saisit du second nombre

som = float(n1) + float(n2) # somme des entiers


print(f"la somme vaut {som}")

# additioner deux nombres a l'aide d'une fonction

def add(a,b):
    """renvoie la somme de deux nombres"""

    return a + b

print(f"la somme des deux nombres vaut :  {add(1,2)}")

# utilisation de la methode add

from operator import add

a = 12
b = 13

s = add(12,13)
print(f"la somme en utilisant la methode add vaut {s}")

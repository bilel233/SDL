# programme python pour imprimer les nombres pairs d'une liste d'entiers

def nombresPairs(L):
    """affiche tout les nombres pairs d'une liste d'entiers"""

    if L == []: # cas ou la liste est vide
        print("rien a afficher, la liste est vide")
    else:   #la liste contient au moins un element

        for k in L:
            if k % 2 == 0:  # on verifie si le nombre est divisible par 2
                print(f"{k} est un nombre pair")
            # ne rien faire on avance
        print()
        print("on a finit de parcourir la liste")

def nombrePairs1(L):
    """

    affiche les entiers pairs dans la liste L
    """

    if L == []:
        print("rien a afficher, la liste est vide")
    else:   #on a au moins un element dans la liste L
        i = 0
        while i < len(L):
            if L[i] % 2 == 0:
                print(f"l'entier pair à l'indice {i} vaut {L[i]}")
            i = i + 1
        print()
        print("on a finit de parcourir la liste ")


if __name__ == "__main__":
    L = [1,2,3,4,5,6,10000,10001]
    nombresPairs(L)
    print("======================")
    print(nombrePairs1(L))









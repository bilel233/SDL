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


if __name__ == "__main__":
    L = [1,2,3,4,5,6,10000,10001]
    nombresPairs(L)









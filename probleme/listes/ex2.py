# trouver la longeur d'une liste en python

def longueur(L):
    """renvoie la longueur d'une liste en python"""

    return len(L)
def methodeNaive(L):
    """
    renvoie la taille de la liste L
    """

    cpt = 0
    for k in L:
        cpt = cpt + 1
    return cpt


if __name__ == "__main__":
    L = [10,20,30]
    print(longueur(L))
    print()
    print(f"avec la methoder naïve, la taille de la liste est : {methodeNaive(L)}")

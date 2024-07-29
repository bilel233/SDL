# recuperer le minimum de deux nombres

from functools import reduce
def minimum(a,b):
    """
    renvoie le minimum de deux nombres
    """

    if a <=b :
        return a
    return b

# en utilisant la fonction min


if __name__=="__main__":
    print(f"le minimum est {minimum(1,2)}")
    print(f"le minimum est {minimum(-1, 2)}")
    print(f"le minimum est {minimum(-1, -4)}")
    print(f"le minimum en utilisant la fonction min est {min(10,9)}")

    # en utilisant la methode sorted()

    a = 12
    b = 3
    L = [a,b]
    L1 = sorted(L)   # on trie la liste de facon croissante
    print(f"la valeur minimale est {L1[0]} ")

    # en utilisant la fonction reduce
    L0 = [1,2,3,10,11,23]
    print(f"le minimum en utilisant la fonction reduce est {reduce(minimum,L0)}")
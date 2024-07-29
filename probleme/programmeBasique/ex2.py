# recuperer le minimum de deux nombres

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
# fonction qui calcule la somme des n premiers entiers

def sommeNPremiersEntiers(n):
    """

    renvoie la somme des n premiers entiers
    """

    if n < 0:
        return
    elif n == 0:
        return 0
    else:
        return n + sommeNPremiersEntiers(n-1)

if __name__ == "__main__":
    print(sommeNPremiersEntiers(0))
    print(sommeNPremiersEntiers(1))
    print(sommeNPremiersEntiers(2))
    print(sommeNPremiersEntiers(3))
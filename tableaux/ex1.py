from array import *

if __name__ == "__main__":
    arr = array('i', [1, 2, 3])
    print(arr)
    # affichage des elements du tableau
    for k in arr:
        print(k,end = " ")

    # ajouter un element a la fin du tableau

    arr.append(10)
    print()
    for k in arr:
        print(k,end = " ")
    # utilisation de la methode insert(i,x)
    arr.insert(2,100)
    print()
    print(arr)
    arr.insert(5, 10000)
    print(arr)
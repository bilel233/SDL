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
    # utilisation de la methode pop()
    print(len(arr))
    arr.pop(3)
    print(f"le tableau avec son element supprimé {arr}")
    # utilisation de la methode remove
    arr.remove(10000)
    print(arr)
    arr.remove(2)
    print(arr)
    # utilisation de la methode reverse
    arr.reverse()
    print(arr)
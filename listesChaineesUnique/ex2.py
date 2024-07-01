# recherche un elements dans une liste chainee unique

class Node:
    """modelisation d'un njoeud d'une liste chainee"""

    def __init__(self, val):
        self.val = val
        self.next = None


class Linkedlist():
    """
    modelisation d'une liste chainee
    """

    def __init__(self):
        self.head = None

    def rechercheElement(self, key):
        """renvoie True si l'element est trouve. False sinon
        """

        if self.head is None:
            return False
        else:
            Q = self.head
            while Q is not None:
                if Q.val == key:
                    return True
                Q = Q.next
            return False

    def ajoutDebutListe(self, val):
        """
        ajoute un noeud au debut de la liste chainee
        """
        n = Node(val)

        if self.head is None:
            n.next = self.head
            self.head = n
        else:  # dans le cas ou la liste chainee n'est pas vide

            n.next = self.head
            self.head = n

    def rechercheElementRecursive(self, key, liste):
        """renvoie True si l'element est present dans la liste chainee.
        False sinon
        """

        if liste is None:
            return False
        elif liste.val == key:
            return True
        else:
            return self.rechercheElementRecursive(key, liste.next)


if __name__ == "__main__":
    L = Linkedlist()
    L.ajoutDebutListe(0)
    L.ajoutDebutListe(1)
    L.ajoutDebutListe(3)
    L.ajoutDebutListe(10)
    print(L.rechercheElement(3))
    print(L.rechercheElement(100))
    print()
    print(L.rechercheElementRecursive(10, L.head))
    print(L.rechercheElementRecursive(2, L.head))
    print(L.rechercheElementRecursive(-3, L.head))
    print(L.rechercheElementRecursive(-1000, L.head))

# trouver la position d'un entier dans une liste doublement chainee

class Node:
    """
    Modelise un noeud d'une liste doublement chainee
    """

    def __init__(self,val):
        """
        Constructeur pour modeliser l'objet Node
        """

        self.val = val
        self.next = None
        self.prec = None
class LinkedList:
    """
    Modelise une liste chainee
    """

    def __init__(self):
        """
        constructeur qui instancie la tete de liste
        """

        self.head = None    # la tete de liste

    def rechercheElement(self,key):
        """

        renvoie la position de l'element dans la liste doublement chainee
        """

        if self.head is None:

            # cas ou la liste est vide
            return
        else:   # la, liste admet au moins un element, un noeud
            i = 0   # le compteur
            q = self.head
            while q is not None:
                if key == q.val:
                    return i
                # autrement, on avance dans la liste chainee
                q = q.next
                i = i + 1
            return -1

    def insertionDebutListe(self,val):
        """
        Insere un noeud au debut de la liste doublement chainee
        """
        n = Node(val)

        if self.head is None:   # cas ou la liste chainee est vide
            self.head = n
        else:
            n.next = self.head
            self.head.prec = n
            self.head = n

    def affichageListe(self):
        """

        affiche les valeurs de la liste
        """

        if self.head is None:
            return
        else:
            q = self.head
            while q is not None:
                print(q.val)
                q = q.next






if __name__=="__main__":
    L = LinkedList()
    L.affichageListe()
    L.insertionDebutListe(10)
    L.affichageListe()
    print()
    L.insertionDebutListe(20)
    L.affichageListe()
    print(L.rechercheElement(10))
    print(L.rechercheElement(11))







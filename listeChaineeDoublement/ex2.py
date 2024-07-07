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

if __name__=="__main__":
    L = LinkedList()
    L.rechercheElement(10)







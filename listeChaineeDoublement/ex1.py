# afficher les elements d'une liste doublement chainee

class Node:
    """
    modelisation d'un noeud d'une liste doublement chainee
    """

    def __init__(self,val):
        self.val = val
        self.next = None
        self.prec = None

class LinkedList:
    """
    modelistation d'une liste chainee
    """

    def __init__(self):
        self.head = None


    def affichageElementsListeChainee(self):
        """

        Affiche les elements de la liste
        """

        if self.head is None:
            return
        else:  # la liste chainee contient au moins un element

            q = self.head
            while q is not None:
                print(f"la valeur du noeud est {q.val}")
                q = q.next
    def insertionDebutListeChainee(self,val):
        """

        insere un noeud au debut de la liste chainee
        """
        n = Node(val)

        if self.head is None:
            self.head = n

        else:
            n.next = self.head
            self.head.prec = n
            self.head = n



if __name__ == "__main__":

    L = LinkedList()
    L.insertionDebutListeChainee(10)
    L.insertionDebutListeChainee(11)
    L.insertionDebutListeChainee(20)
    L.insertionDebutListeChainee(121)
    L.affichageElementsListeChainee()



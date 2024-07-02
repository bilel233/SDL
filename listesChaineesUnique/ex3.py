# inserer un noeud dans une liste chainee


class Node:
    """
    modelisation d'un noeud d'une liste chainee
    """

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    """
    modelisation d'une liste chainee
    """

    def __init__(self):
        self.head = None

    def ajoutDebutListe(self, val):
        """
        ajoute un noeud au debut d'une liste chainee
        """
        n = Node(val)

        if self.head is None:
            n.next = self.head
            self.head = n
        else:  # cas ou la liste chainee n'est pas vide

            n.next = self.head
            self.head = n

    def ajoutApresNoeuds(self, precNoeuds, val):
        """
        Ajoute un noeud apres un noeuds donne dans une liste chainee
        """
        n = Node(val)

        if self.head is None or precNoeuds is None:
            print("impossible d'inserer le noeud")
        else:
            n.next = precNoeuds.next
            precNoeuds.next = n
    def ajoutNoeudsFinListe(self,val):
        """
        Ajoute un noeud à la fin d'une liste chainee
        """

        n = Node(val)
        if self.head is None:
            self.head = n
            print("insertion du noeud dans la cas ou la liste chainee est vide")
        q = self.head
        while q.next is not None:
            q = q.next
        q.next = n


    def parcourtNoeud(self):
        """Parcourt les elements d'une liste chainee"""

        if self.head is None:
            print("La liste chainee est vide. Rien a afficher")
        else:
            q = self.head
            while q is not None:
                print(f"la valeur du noeud est {q.val}")
                q = q.next
            print("le parcourt des noeuds est finit")


if __name__ == "__main__":
    L = LinkedList()
    L.ajoutDebutListe(0)
    L.ajoutDebutListe(1)
    L.parcourtNoeud()
    print("creation d'une liste chaineen manuellement")
    print()
    LChainee = LinkedList()
    n1 = Node(10)
    n2 = Node(11)
    n3 = Node(12)
    n4 = Node(13)
    LChainee.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    LChainee.parcourtNoeud()
    print()
    LChainee.ajoutApresNoeuds(n2, 11.5)
    LChainee.parcourtNoeud()
    print()
    LChainee.ajoutApresNoeuds(n3, 12.98)
    LChainee.parcourtNoeud()
    print()
    LChainee.ajoutNoeudsFinListe(14)
    LChainee.parcourtNoeud()
    print()
    LChainee.ajoutNoeudsFinListe(15)
    LChainee.parcourtNoeud()

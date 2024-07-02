class Node:
    """modelisation d'un noeud d'une liste chainee"""

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    """
    modelisation d'une liste chainee
    """

    def __init__(self):
        self.head = None

    def suppresionNoeudsDebut(self):
        """

        Supprime un noeud du debut de la liste chainee
        """

        if self.head is None:  # la tete de liste est vide
            print("Rien a supprimer, la liste chainee est vide")
        else:  # la tete d eliste n'est pas vide
            self.head = self.head.next
        print("On a deplace la tete de liste")

    def ajoutNoeudsDebut(self, val):
        """

        Ajoute un noeud au debut de la liste chainee
        """

        n = Node(val)

        if self.head is None:
            self.head = n
        else:
            n.next = self.head
            self.head = n
        print("ajout du noeud au debut de la liste chainee")

    def affichageElementsNoeud(self):
        """

        Affiche les noeuds d'une liste chainee
        """

        if self.head is None:
            print("Rien a afficher, la liste est vide")
        else:
            q = self.head
            while q is not None:
                print(f"la valeur du noeud est {q.val}")
                q = q.next
            print("on a finit de parcourir la liste chainee")

    def suppressionNoeudFin(self):
        """

        suprime un noeud a la fin d'une liste chainee

        """
        if self.head is None:
            print("Rien a supprimer car aucun noeud dans la liste chainee")
        else:
            p = self.head
            q = self.head.next
            while q.next is not None:
                p = p.next
                q = q.next
            p.next = None



if __name__ == "__main__":
    L = LinkedList()
    L.ajoutNoeudsDebut(10)
    L.affichageElementsNoeud()
    print()
    L.ajoutNoeudsDebut(11)
    L.affichageElementsNoeud()
    print()
    L.suppresionNoeudsDebut()
    L.affichageElementsNoeud()
    L.ajoutNoeudsDebut(11)
    L.ajoutNoeudsDebut(12)
    L.ajoutNoeudsDebut(13)
    L.affichageElementsNoeud()
    print()
    L.suppressionNoeudFin()
    L.affichageElementsNoeud()
    print()

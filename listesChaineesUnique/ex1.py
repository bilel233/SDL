# affichage des elements d'une liste chainee unique

class Node:
    """modelisation d'un noeud d'une liste chainee"""

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList():
    """modelisation d'une liste chainee unique"""

    def __init__(self):
        self.head = None

    def affichageNoeud(self):
        """affiche les elements de la liste chainee"""

        if self.head is None:  # cas ou la tete de noeuds est vide
            print("rien n'a afficher. La liste est vide")
        else:
            Q = self.head
            while Q is not None:
                print(f"la valeur du noeud est {Q.val}")
                Q = Q.next
            print()
            print("On a finit de parcourir la liste chainee")

    def ajoutDebutListe(self, val):
        """ajoute  un noeud au debut de la liste chainee"""

        n = Node(val)
        n.next = self.head
        self.head = n


if __name__ == "__main__":
    L = LinkedList()
    L.ajoutDebutListe(0)
    L.ajoutDebutListe(1)
    L.ajoutDebutListe(9)
    L.affichageNoeud()

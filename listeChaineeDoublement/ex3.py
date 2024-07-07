# insertion d'un noeud apres une position dans une liste doublement chainee

class Node:
    """
    modelisation d'un noeud dans une liste doublement chainee
    """

    def __init__(self,val):
        self.val = val
        self.suivant = None
        self.precedent = None
class LinkedList:
    """
    modleisation d'une liste chainee
    """
    def __init__(self):
        self.head = None

    def insertionDebutListe(self,val):
        """

        insere un noeud au debut de la liste chainee
        """

        n = Node(val)
        if self.head is None:
            self.head = n
        else:   # cas ou la tete de liste n'est pas vide
            self.head.precedent = n
            n.suivant = self.head
            self.head = n


    def affichageElementListe(self):
        """

        affiche les elements d'une liste doublement chainee
        """

        if self.head is None:   # cas ou la liste doublement chainee est vide
            return
        else:
            q = self.head
            while q is not None:    # on parcourt la liste chainee
                print(q.val)
                q = q.suivant









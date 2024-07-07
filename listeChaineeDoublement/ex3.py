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

    def insertionPositionNoeud(self,pos,val):
        """

        Insere un noeud a une position specifique
        dans la liste
        """
        n = Node(val)


        if self.head is None:   # cas ou la tete de liste est vide
            self.head = n
        else:
            i = 0
            q = self.head
            l = self.head.suivant
            while i < pos-1:
                q = q.suivant
                l = l.suivant
                i+=1
            q.suivant = n
            n.precedent = q
            n.suivant = l
            l.precedent = n




if __name__ == "__main__":
    L = LinkedList()
    L.insertionDebutListe(10)
    L.insertionDebutListe(9)
    L.insertionDebutListe(8)
    L.insertionDebutListe(7)
    L.insertionDebutListe(6)
    L.insertionDebutListe(5)
    L.insertionDebutListe(4)
    L.insertionDebutListe(3)
    L.insertionDebutListe(2)
    L.insertionDebutListe(1)
    L.insertionDebutListe(0)
    L.affichageElementListe()
    print("===================================")
    L.insertionPositionNoeud(8,1000000)
    L.affichageElementListe()








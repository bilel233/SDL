# liste chainee circulaire


class Node:
    """representation d'un noeud d'une liste chainee circulaire"""

    def __init__(self,val):
        self.val = val
        self.next = None

class ListeChaineeCirculaire:
    """modelisation de la liste chainee circulaire"""

    def __init__(self):
        self.last  = Node

    def insertionListeVide(self,val):
        """Insert un noeud dans la liste chainee circulaire"""

        if self.last is not None:
            return self.last

        n = Node(val)
        self.last = n
        self.last.next = self.last
        return self.last
if __name__ == "__main__":

    L = ListeChaineeCirculaire()
    L.insertionListeVide(10)






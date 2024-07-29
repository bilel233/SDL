# liste chainee circulaire


class Node:
    """representation d'un noeud d'une liste chainee circulaire"""

    def __init__(self, val):
        self.val = val
        self.next = None


class ListeChaineeCirculaire:
    """modelisation de la liste chainee circulaire"""

    def __init__(self):
        self.last = None

    def insertionListeVide(self, val):
        """Insert un noeud dans la liste chainee circulaire"""

        if self.last is not None:
            return self.last

        n = Node(val)
        self.last = n
        self.last.next = self.last
        #print(self.last.val)
        return self.last

    def insertionDebutListeChaineeCirculaire(self, val):
        """Insere un noeud au debut de la liste chainee circulaire"""

        if self.last is None:
            self.insertionListeVide(val)
        n = Node(val)
        n.next = self.last.next
        self.last = n


if __name__ == "__main__":
    L = ListeChaineeCirculaire()
    L.insertionDebutListeChaineeCirculaire(100)
    print(L.last.val)
    L.insertionDebutListeChaineeCirculaire(101)
    print(L.last.val)
    print(L.last.next.val)

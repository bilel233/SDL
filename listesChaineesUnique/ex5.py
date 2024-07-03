# trouver  le milieu d'une liste chainee unique

class Node:
    """
    modelisation d'une liste chainee unique
    """

    def __init__(self,val):
        self.val = val
        self.next = None


class LinkedList:
    """
    modelisation d'une liste chainee
    """

    def __init__(self):
        self.head = None

    def insertionAuDebutNoeuds(self,val):
        """

        Insere un noeud au debut de la liste chainee
        """
        n = Node(val)


        if self.head is None:
            self.head = n
        else:
            n.next = self.head
            self.head = n
        print("Insertion du noeud reussi")

    def longueurListeChainee(self):
        """

        renvoie la longueur de la liste chainee
        """
        l = 0
        if self.head is None:
            return 0
        else:
            q = self.head
            while q is not None:
                l+=1
                q = q.next
            return l



    def getMilieuNoeuds(self):
        """renvoie le noeud du milieu"""

        if self.head is None:
            print("la liste chainee est vide. rien a renvoyer")
            return
        else:
            q = self.head
            l = self.longueurListeChainee()
            iMilieu = l // 2
            while iMilieu > 0:
                q = q.next
                iMilieu = iMilieu - 1
            return q

if __name__ == "__main__":
    L = LinkedList()
    L.insertionAuDebutNoeuds(1)
    L.insertionAuDebutNoeuds(2)
    L.insertionAuDebutNoeuds(3)
    L.insertionAuDebutNoeuds(4)
    L.insertionAuDebutNoeuds(5)
    L.insertionAuDebutNoeuds(6)
    L.insertionAuDebutNoeuds(7)
    L.insertionAuDebutNoeuds(8)
    n = L.getMilieuNoeuds()
    print(f"la valeur du noeud est {n.val}")



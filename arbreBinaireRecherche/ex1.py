# insertion d'un noeud donné dans un arbre binbaire de recherche

class Node:
    """modelisation d'un noeud dans un arbre binaire de recherche"""

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insertionNoeud(val,root):
    """
    insere un noeud dans un arbre binaire de recherche

    """

    if root is None:
        return Node(val)
    else:
        if val < root.val:
            root.left = insertionNoeud(val,root.left)
        else:
            root.right = insertionNoeud(val, root.right)
    return root



if __name__ == "__main__":
    root = Node(20)
    insertionNoeud(21,root)
    insertionNoeud(19, root)
    insertionNoeud(17, root)
    insertionNoeud(50, root)








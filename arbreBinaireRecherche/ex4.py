# rechercher un noeud specifique dans un arbre binaire de recherche

class Node:
    """
    modelisation d'un noeud d'un arbre binaire de recherche
    """

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def rechercheNoeud(root,val):
    """

    recherche un noeud specifique dans un arbre binaire de recherche
    """

    if root is None or root.val == val:
        return root

    else:
        if val < root.val:
            return rechercheNoeud(root.left,val)
        elif val > root.val:
            return rechercheNoeud(root.right,val)


def insertionNoeuds(root,val):
    """

    insere un noeud dans un arbre binaire de recherche
    """

    if root is None:
        return
    else:
        if val < root.val:
            root.left = insertionNoeuds(root.left,val)
        elif val > root.val:
            root.right = insertionNoeuds(root.right, val)
    return root

if __name__ == "__main__":
    root = Node(20)
    insertionNoeuds(root,19)
    insertionNoeuds(root,21)
    n = rechercheNoeud(root, 21)





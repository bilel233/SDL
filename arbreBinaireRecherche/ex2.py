#inserer un noeud dans un arbre binaire

class Node:
    """
    modelisation d'un noeud d'un arbre binaire de recherche
    """

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def insertionNoeuds(root,val):
    """insere un noeud dans un arbre binaire de recherche"""

    if root is None:
        return Node(val)
    # l'arbre binaire n'est pas vide

    if val < root.val:
        root.left = insertionNoeuds(root.left,val)
    elif val > root.val:
        root.right = insertionNoeuds(root.right,val)
    return root

if __name__ == "__main__":
    root = Node(20)
    insertionNoeuds(root,21)
    print(root.right.val)
    insertionNoeuds(root,17)
    print(root.left.val)
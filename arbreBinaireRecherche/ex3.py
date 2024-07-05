# affichage des noeuds d'un arbre binaire de maniere transversale

class Node:
    """
    Modelisation d'un noeud d'un arbre binaire
    """

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insertionNoeuds(root,val):
    """

    insert un noeud dans un arbre binaire de recherche
    """

    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insertionNoeuds(root.left,val)
    elif val > root.val:
        root.right = insertionNoeuds(root.right,val)

    return root

def affichageNoeud(root):
    """affiche les noeuds d'un arbre binaire de recherche"""

    if root is None:
        print("rien a afficher, l'arbre binaire est vide")
    else:
        affichageNoeud(root.left)
        print(f"la valeur du noeud est {root.val}")
        affichageNoeud(root.right)

if __name__ == "__main__":
    root = Node(30)
    insertionNoeuds(root,12)
    insertionNoeuds(root, 11)
    insertionNoeuds(root, 10)
    insertionNoeuds(root, 13)
    insertionNoeuds(root, 14)
    insertionNoeuds(root, 15)
    affichageNoeud(root)

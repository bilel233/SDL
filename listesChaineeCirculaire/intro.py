# representation d'une liste chainee circulaire

class Node:
    """Modelisation d'une liste chainee circulaire"""

    def __init__(self,val):
        self.val = val
        self.next = None


if __name__=="__main__":
    n1 = Node(10)
    n2 = Node(9)
    n3 = Node(8)

    n1.next = n2
    n2.next = n3
    n3.next = n1

    print(f"la valeur du noeud n1 est : {n1.val}")
    print(f"la valeur du noeud n2 est : {n2.val}")
    print(f"la valeur du noeud n3 est : {n3.val}")
    print("=======================================")
    print(f"{n3.next.val}")
    print(f"{n1.next.val}")
    print(f"{n2.next.val}")

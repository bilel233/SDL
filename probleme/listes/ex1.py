# echanger le premier et le dernier element d'une liste

def intervertir(L):
    """intervertit le premier et le dernier element d'une liste L"""

    n = len(L)
    temp = L[0]
    L[0] = L[n-1]
    L[n-1] = temp
    print(L)

def intervertir1(L):
    """
    intervertit le premier et dernier element d'une liste L
    """

    L[0],L[-1] = L[-1],L[0]
    print(f"la liste intervertit vaut {L}")

if __name__ == "__main__":
    intervertir([12,35,9,56,24])
    print()
    intervertir1([12,35,9,56,24])


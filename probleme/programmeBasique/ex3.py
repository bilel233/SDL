# programme python pour calculer le pgcd de deux nombres


from math import *

pgcd = gcd(3,2)
print(f"le pgcd entre 3 et 2 est {pgcd}")
print(f"le pgcd entre 6 et 4 est {gcd(6,4)}")
print(f"le pgcd entre 60 et 48 est {gcd(60,48)}")

# en utilisant la methode recursif

def recusivePgcd(a,b):
    """renvoie le pgc de deux entiers"""

    if b == 0:
        return a
    return recusivePgcd(b,a%b)

if __name__ == "__main__":
    print(f"le pgcd entre a et b vaut {recusivePgcd(60,48)}")
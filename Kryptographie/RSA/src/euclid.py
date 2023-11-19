# Implementation of EA
def gcd(p, q):
    while q != 0:
        (p, q) = (q, p % q)
    return p

# Implementation of the EEA
def extgcd(r0, r1):
    u, v, s, t = 1, 0, 0, 1
    changed = False
    # Swap arguments if r1 is smaller
    if r1 < r0:
        temp = r1
        r1 = r0
        r0 = temp
        changed = True
    # While Loop to compute params
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        u, s = s, u - q * s
        v, t = t, v - q * t
    if changed == True:
        return r0, u, v
    else:
        return r0, v, u

# User Interface function
def main():
    print("Geben sie r0 ein: ")
    r0 = int(input())
    print("Geben sie r1 ein: ")
    r1 = int(input())

    print("----- Ergebnis ----")

    a1, u1, v1 = extgcd(r0, r1)
    print("GCD: ", a1)
    print("s: ", u1)
    print("t: ", v1)

if __name__ == "__main__":
    main()
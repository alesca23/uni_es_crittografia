import math

def shanks(p, n, a, b):
    # m = ⌈√n⌉
    m = math.ceil(math.sqrt(n))
    
    # Baby Steps: calcolo a^(mj) per j da 0 a m-1
    L1 = {}
    a_m = pow(a, m, p)  # Calcola a^m una volta
    a_mj = 1
    for j in range(m):
        L1[a_mj] = j
        a_mj = (a_mj * a_m) % p
    
    # Giant Steps: calcolo b*a^(-i) e cerco collisioni
    a_inv = pow(a, -1, p)
    gamma = b
    for i in range(m):
        if gamma in L1:  # Collisione trovata
            j = L1[gamma]
            x = (m * j + i) % n
            return x
        gamma = (gamma * a_inv) % p
    
    return None


if __name__ == "__main__":
    p = 24691
    a = 106
    b = 12375
    n = p - 1

    x = shanks(p, n, a, b)
    print(f"Logaritmo discreto trovato: {x}")
    print(f"Verifica: {a}^{x} mod {p} = {pow(a, x, p)}")
    
    
    p = 458009
    a = 6
    b = 248388
    n = p - 1

    x = shanks(p, n, a, b)
    print(f"\nLogaritmo discreto trovato: {x}")
    print(f"Verifica: {a}^{x} mod {p} = {pow(a, x, p)}")

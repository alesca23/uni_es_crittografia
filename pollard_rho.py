import math

def f(x, a, b, p, n, alpha, beta):
    partition = x % 3
    
    if partition == 1:  # x ∈ S1
        x_new = (beta * x) % p
        a_new = a
        b_new = (b + 1) % n
    elif partition == 0:  # x ∈ S2
        x_new = (x * x) % p
        a_new = (2 * a) % n
        b_new = (2 * b) % n
    else:  # x ∈ S3
        x_new = (alpha * x) % p
        a_new = (a + 1) % n
        b_new = b
    
    return (x_new, a_new, b_new)


def pollard_rho_discrete_log(p, n, alpha, beta):    
    # (x, a, b) ← f(1, 0, 0)
    x, a, b = f(1, 0, 0, p, n, alpha, beta)
    print(f"(x, a, b) = f(1, 0, 0) = ({x}, {a}, {b})")
    
    # (x', a', b') ← f(x, a, b)
    x_primo, a_primo, b_primo = f(x, a, b, p, n, alpha, beta)
    print(f"(x', a', b') = f({x}, {a}, {b}) = ({x_primo}, {a_primo}, {b_primo})")

    
    i = 0
    while x != x_primo:
        i += 1
        
        # (x, a, b) ← f(x, a, b)
        x, a, b = f(x, a, b, p, n, alpha, beta)
        
        # (x', a', b') ← f(x', a', b')
        x_primo, a_primo, b_primo = f(x_primo, a_primo, b_primo, p, n, alpha, beta)
        
        # (x', a', b') ← f(x', a', b')
        x_primo, a_primo, b_primo = f(x_primo, a_primo, b_primo, p, n, alpha, beta)
    
    print(f"\nCollisione trovata dopo {i} iterazioni")
    print(f"x = {x}, a = {a}, b = {b}")
    print(f"x' = {x_primo}, a' = {a_primo}, b' = {b_primo}")
    print()
    
    # se gcd(b' - b, n) ≠ 1 return False
    diff_b = (b_primo - b) % n
    gcd_value = math.gcd(diff_b, n)
    
    print(f"Verifica condizione di invertibilità:")
    print(f"b' - b = {b_primo} - {b} = {diff_b} (mod {n})")
    print(f"gcd(b' - b, n) = gcd({diff_b}, {n}) = {gcd_value}")
    
    if gcd_value != 1:
        print(f"\nFALLIMENTO: gcd ≠ 1, impossibile invertire")
        return False
    
    print(f"gcd = 1, si può invertire")
    print()
    
    # altrimenti return ((a - a')(b' - b)^(-1) mod n)
    diff_a = (a - a_primo) % n
    inv_diff_b = pow(diff_b, -1, n)
    result = (diff_a * inv_diff_b) % n
    
    print(f"Calcolo del logaritmo discreto:")
    print(f"  a - a' = {a} - {a_primo} = {diff_a} (mod {n})")
    print(f"  (b' - b)^(-1) = {diff_b}^(-1) = {inv_diff_b} (mod {n})")
    print(f"  log_a(b) = (a - a') × (b' - b)^(-1)")
    print(f"           = {diff_a} × {inv_diff_b}")
    print(f"           = {result} (mod {n})")
    
    return result


if __name__ == "__main__":
    p = 458009
    alpha = 2
    beta = 56851
    n = 57251

    result = pollard_rho_discrete_log(p, n, alpha, beta)

    if result:
        print("RISULTATO FINALE")
        print(f"log 56851 = {result} (mod {n})")
        print()
        
        # Verifica
        print("VERIFICA:")
        verification = pow(alpha, result, p)
        print(f"  2^{result} mod {p} = {verification}")
        
        if verification == beta:
            print(f"CORRETTO: {verification} = {beta}")
        else:
            print(f"ERRORE: Atteso {beta}, ottenuto {verification}")
    else:
        print("\nAlgoritmo terminato con fallimento")
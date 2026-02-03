def lcg(seed, a, c, m, n=10):
    """Génère n nombres avec LCG."""
    results = [seed]
    state = seed
    for i in range(n):
        state = (a * state + c) % m
        results.append(state)
    return results


def recover_a(x0, x1, x2, m):
    """Récupère 'a' à partir de 3 sorties consécutives."""
    numerator = (x2 - x1) % m
    denominator = (x1 - x0) % m
    inv = pow(denominator, -1, m)
    return (numerator * inv) % m


def recover_c(x0, x1, a, m):
    """Récupère 'c' à partir de 2 sorties consécutives."""
    return (x1 - a * x0) % m


def recover_previous(x, a, c, m):
    """Calcule la valeur précédente dans la séquence LCG."""
    inv_a = pow(a, -1, m)
    return (inv_a * (x - c)) % m


def recover_seed(outputs, start_index, a, c, m):
    current = outputs[start_index]
    
    # Remonter étape par étape jusqu'à l'index 0
    for i in range(start_index):
        current = recover_previous(current, a, c, m)
    
    return current


# --- Démonstration ---

# Paramètres secrets
a_secret = 6364136223846793005
c_secret = 1442695040888963407
m = 2**64
seed_secret = 12345

# Génération complète
outputs = lcg(seed_secret, a_secret, c_secret, m, n=10)

print("Séquence complète :")
for i, x in enumerate(outputs):
    print(f"  X{i} = {x}")

# --- Attaque avec sorties aux index 6, 7, 8 ---
print("\n=== Attaque avec X6, X7, X8 ===")

start_index = 6
x0 = outputs[start_index]
x1 = outputs[start_index + 1]
x2 = outputs[start_index + 2]

print(f"Sorties interceptées : X{start_index}={x0}, X{start_index+1}={x1}, X{start_index+2}={x2}")

# Récupération des paramètres
a_recovered = recover_a(x0, x1, x2, m)
c_recovered = recover_c(x0, x1, a_recovered, m)
seed_recovered = recover_seed(outputs, start_index, a_recovered, c_recovered, m)

print(f"\na récupéré : {a_recovered}")
print(f"c récupéré : {c_recovered}")
print(f"Graine récupérée : {seed_recovered}")

print(f"\nAttaque réussie : {seed_recovered == seed_secret}")

# --- Test avec d'autres positions ---
print("\n=== Test avec différentes positions ===")

for start in [1, 3, 5, 8]:
    x0 = outputs[start]
    x1 = outputs[start + 1]
    x2 = outputs[start + 2]
    
    a_rec = recover_a(x0, x1, x2, m)
    c_rec = recover_c(x0, x1, a_rec, m)
    seed_rec = recover_seed(outputs, start, a_rec, c_rec, m)
    
    print(f"  Depuis X{start}, X{start+1}, X{start+2} : graine = {seed_rec}")
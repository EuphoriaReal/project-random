import random
import math


def box_muller():

    while True:
        u1 = 2.0 * random.random() - 1.0 
        u2 = 2.0 * random.random() - 1.0
        s = u1 * u1 + u2 * u2
        
        if s != 0.0 and s < 1.0:
            break
    
    w = math.sqrt(-2.0 * math.log(s) / s)
    g1 = u1 * w
    g2 = u2 * w
    
    return g1, g2


def generate_normal(n, mean, stddev):

    results = []
    cache = None
    
    for i in range(n):
        if cache is None:
            g1, g2 = box_muller()
            results.append(mean + g1 * stddev)
            cache = g2
        else:
            results.append(mean + cache * stddev)
            cache = None
    
    return results

# Génération avec moyenne et écart-type personnalisés
print("\n10 nombres N(100, 15²) :")
nombres_qi = generate_normal(10, mean=100, stddev=15)
for i, x in enumerate(nombres_qi, 1):
    print(f"  {i}: {x:.6f}")

# Vérification statistique
print("\n--- Vérification statistique (10000 échantillons) ---")
echantillons = generate_normal(10000, mean=0, stddev=1)
moyenne = sum(echantillons) / len(echantillons)
variance = sum((x - moyenne) ** 2 for x in echantillons) / len(echantillons)
ecart_type = math.sqrt(variance)

print(f"Moyenne observée : {moyenne:.4f} (attendu : 0)")
print(f"Écart-type observé : {ecart_type:.4f} (attendu : 1)")
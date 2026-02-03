
def lcg(seed, a, c, m):
    results = [seed]
    
    for i in range(10):
        seed = (a * seed + c) % m
        results.append(seed)
    
    return results

nombres_minstd = lcg(seed=12345, a=48271, c=0, m=2**31 - 1)
print(nombres_minstd)

nombres_mmix = lcg(seed=12345, a=6364136223846793005, c=1442695040888963407, m=2**64)
print(nombres_mmix)


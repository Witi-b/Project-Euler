possible_triplets = []
triplets = []

for c in range(4, 996):
    for b in range(2, 994):
        for a in range(1, 993):
            if a+b+c == 1000:
                if (a**2 + b **2) == (c**2):
                    triplets.extend([c,b,a])
                    possible_triplets.append(triplets.copy())
                    triplets.clear()
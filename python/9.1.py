sum = 1000
for a in range(3, (sum-3)//3):
    for b in range(a+1, (sum-1-a)//2):
        c = sum-a-b
        if (c*c == a*a + b*b):
            print(f"{a*b*c}")
from math import gcd, ceil, sqrt
sum = 1000000
sum2 = sum//2
mlimit = ceil(sqrt(sum2)) - 1
for m in range(2, mlimit):
    if sum2 % m == 0:
        sm = sum2 // m
        while sm % 2 == 0:
            sm = sm //  2
        if m % 2 == 1:
            k = m + 2
        else: k = m + 1
        while (k < 2*m) and (k <= sm):
            if (sm % k == 0) and (gcd(k,m) == 1):
                d = sum2 // (k*m)
                n = k - m
                a = d*(m*m-n*n)
                b = 2*d*m*n
                c = d*(m*m+n*n)
                print(f"{a}, {b}, {c}")
                print(f"a*b*c = {a*b*c}")
            k += 2
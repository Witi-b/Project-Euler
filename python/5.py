import math
k = 20
N = 1
x = 1
check = True
primes = list()
limit = k**(1/2)

lower = 1
upper = k

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primes.append(num)
i = 0
while i < len(primes):
    while primes[i] <= k:
        exp = 1
        if check == True:
            if primes[i] <= limit:
                exp = math.floor( math.log(k) / math.log(primes[i]) )
            else:
                check = False
        N = N * primes[i]**exp
        i += 1
        if i >=len(primes):
            break
print(N)
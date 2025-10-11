#For the smallest positive number that is evenly divisible in some range, you need to multiple by the primes and the largest squares/cubes/etc. containing the smallest primes found in that range. For example, for the smallest number that can be divided between 1 and 10, you would multiply the numbers 9, 8, 7, and 5 to get 2520.

g = int(input("What is the largest number for the range?: "))
num = g
primes = list()
exponentials = list()
multiples = list()
while num != 1:
    for i in range(2,(num//2)+1):
        if (num % i) == 0:
            num = num - 1
        else:
            primes.append(num)
            num = num - 1
        if num == 3:
            primes.append(num) #adds 3 to the prime list
            num = num - 1
        if num == 2:
            primes.append(num) #adds 2 to the prime list
            num = num - 1
primes.reverse()
num = g
for i in primes:
    power = 2
    perf = i**power
    while perf in range(1,num+1):
        if perf % last == 0:
            exponentials.remove(last)
        exponentials.append(perf)
        last = perf
        power += 1
        perf = i**power
        
        
print(exponentials)
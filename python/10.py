#Find the sum of all the primes below 2 million
#Very slow

PRIMES = [2,3,5]
SUM = 10

def prime_list(n):
    global SUM
    numb = 7
    while numb < n:
        if prime(numb):
            SUM += numb
            numb += 2
        else:
            numb += 2
    return PRIMES

def prime(n):
    is_prime = True
    for numb in PRIMES:
        if n % numb == 0:
            is_prime = False
            break
    if is_prime:
        PRIMES.append(n)
    return is_prime


number = int(input("Enter a number: "))
prime_list(number)
print(SUM)
#Create an array of primes to test instead of testing every number

PRIMES = [2,3,5]

def nth_prime_number(n):
    prime_count = 3
    numb = 7
    while prime_count != n:
        if prime(numb):
            prime_count += 1
            nth_prime = numb
            numb += 2
        else:
            numb += 2
            
    return nth_prime

def prime(n):
    is_prime = True
    for numb in PRIMES:
        if n % numb == 0:
            is_prime = False
            break
    if is_prime == True:
        PRIMES.append(n)
    return is_prime


number = input("Enter a number: ")
print(nth_prime_number(number))
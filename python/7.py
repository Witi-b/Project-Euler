# Currently very slow 

def nth_prime_number(n):
    prime_count = 1
    numb = 1
    while prime_count != n:
        if prime(numb):
            prime_count += 1
            nth_prime = numb
            numb += 1
        else:
            numb += 1
            
    return nth_prime

def prime(n):
    is_prime = True
    numb = 2
    while numb < n:
        if n % numb == 0:
            is_prime = False
            break
        else:
            numb += 1
    return is_prime
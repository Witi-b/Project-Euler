#Find the first triangle number with n factors
#Usage: python3 12.py n
#where n is the number of factors needed to find
import sys
import math

def factors(j):
    #Return the number of factors of an integer j
    n_factors = 0
    #Became much faster when only testing integers up to the square root of j
    for k in range(1, int(math.floor(math.sqrt(j))+1)):
        if j % k == 0 & k != j // k:
            if k <= j // 2 and (j // k) <= (j // 2):
                n_factors += 2
            else:
                n_factors += 2
        elif j % k == 0 & k == j // k:
            #Case where k is square root of j
            n_factors += 1
    print(f"{j} has {n_factors} factors:")
    return n_factors

def main():
    n = int(sys.argv[1])
    triangle_number = 1
    i = 2
    while True:
        triangle_number = triangle_number + i
        i += 1
        if factors(triangle_number) >= n:
            print(f"The first triangle number with over {n} factors is: {triangle_number}")
            break


if __name__ == "__main__":
    main()
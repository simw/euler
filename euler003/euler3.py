#!/usr/bin/python

def test_prime(primes, i):
    for n in primes:
        if i % n == 0:
            return False
        
    return True

def append_prime(primes):
    if primes[-1] == 2:
        primes.append(3)
        return 3
    
    is_prime = False
    i = primes[-1]
    while not is_prime:
        i += 2
        is_prime = test_prime(primes, i)
        
    primes.append(i)
    return i

def prime_factors(i):
    """ Assume that i > 3 """
    primes = [2]
    factors = []
    
    while i > 1:
        n = primes[-1]
        multiplicity = 0
        while i % n == 0:
            i /= n
            multiplicity += 1
            
        if multiplicity > 0:
            factors.append([n, multiplicity])

        append_prime(primes)
        
    return factors

def main():
    result = prime_factors(600851475143)
    print(result)
    print(result[-1][0])
    
    total = 1
    for n in result:
        total *= n[0]**n[1]
        
    print(total)
    
if __name__ == '__main__':
    main()
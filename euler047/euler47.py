from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

def generate_primes(n_max, callback_fn):
    numbers = [i for i in range(0, n_max)]
    primes = []

    i = 1
    while 1:
        num = 0
        # Get next prime number from the list
        try:
            while num == 0:
                i = i + 1
                num = numbers[i]
        except IndexError as e:
            break

        # Remove all multiples of this prime from the remaining list
        mult = num * i
        step = 2 * num
        if num == 2:
            step = num 

        while 1:
            try:
                numbers[mult] = 0
                mult = mult + step
            except IndexError as e:
                break

        # Process this prime number
        if callback_fn:
            finished = callback_fn(num)
            if finished:
                break
        else:
            primes.append(num)

    if primes:
        return primes


def consecutive_prime_factors(n_max, n_consec):
    prime_factors = [[] for i in range(n_max)]    

    def test_consecutives(i):
        found = True
        for j in range(n_consec):
            if i + j >= n_max:
                found = False
                break

            if len(prime_factors[i+j]) != n_consec:
                found = False
                break

        return found

    def add_to_prime_factors(prime):
        # Add multiples of this prime to prime factors list
        mult = prime

        while 1:
            try:
                prime_factors[mult].append(prime)
                mult = mult + prime 
            except IndexError as e:
                break
    
    generate_primes(n_max, add_to_prime_factors)
    for i in range(n_max):
        if test_consecutives(i):
            res = i
            break

    print(res)
    for i in range(n_consec):
        print(prime_factors[res+i])

def main():
    n_max = 1000000
    l = 4
    consecutive_prime_factors(n_max, l)

if __name__ == '__main__':
    main() 

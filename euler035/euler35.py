from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

def generate_primes(n_max, callback_fn):
    numbers = [i for i in range(0, n_max)]
    primes = set() 

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
            primes.add(num)

    if primes:
        return primes

def is_rotatable(prime, primes):
    prime_string = '{0}'.format(prime)
    rotations = set() 
    for i in range(len(prime_string)):
        rotations.add(int(prime_string[i:] + prime_string[:i]))

    for rot in rotations:
        if not rot in primes:
            return None 

    return rotations

def get_rotatables(n_max):
    primes = generate_primes(n_max, None)
    rotatables = [] 
    
    for prime in primes:
        if prime in rotatables:
            continue

        rotations = is_rotatable(prime, primes)
        if rotations:
            for rot in rotations:
                rotatables.append(rot)

    return rotatables

def main():
    n_max = 100
    res = get_rotatables(n_max)
    print(res)
    print(len(res))

    n_max = 1000000
    res = get_rotatables(n_max)
    print(len(res))

if __name__ == '__main__':
    main()
 

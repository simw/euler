from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

def remove_mults(numbers, num, offset):
    # Sets all multiples of num in numbers to 0, starting from num**2
    # Numbers are successive integers, starting from offset

    if num * num - offset < 0:
        rem = offset % num
        if rem == 0:
            mult = 0
        else:
            mult = num - rem
    else:
        mult = num * num - offset

    # step = 2 * num
    # if num == 2:
    step = num 
    while 1:
        try:
            numbers[mult] = 0        
            mult = mult + step 
        except IndexError as e:
            break

def next_primes(n_min, n_max, prev_primes=None, callback=None):
    # Manually exclude 0 and 1
    if n_min < 2:
        n_min = 2

    # Includes n_min, excludes n_max
    numbers = [i for i in range(n_min, n_max)]
    primes = [] 

    # If we don't have the previous primes, need to generate them
    if prev_primes == None:
        if n_min > 2:
            prev_primes = next_primes(2, n_min, None, None)
            primes = []
        else:
            prev_primes = []
            primes = []
    else:
        primes = prev_primes

    # Remove all multiples of prev_primes from the list
    for num in prev_primes:
        remove_mults(numbers, num, n_min)
            
    i = 0
    while 1:
        num = 0
        # Get next prime number from the list
        try:
            while num == 0:
                num = numbers[i]
                i = i + 1
        except IndexError as e:
            break

        # Remove all multiples of this prime from the remaining list
        remove_mults(numbers, num, n_min)
        
        # Process this prime number
        if callback:
            finished = callback(num)
            if finished:
                break
        primes.append(num)

    return primes

def generate_primes(n_max, callback):
    STEP = int(3e7)
    upper = 0
    primes = []
    while upper < n_max:
        lower = upper
        upper = min(upper + STEP, n_max)
        next_primes(lower, upper, primes, callback) 
       
    return primes

def generate_primes_old(n_max, callback_fn):
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

def compare_prime_generators():
    n = int(1e7) 
    print(len(generate_primes(n, None)))
    print(len(generate_primes_old(n, None)))

if __name__ == '__main__':
    compare_prime_generators()
 

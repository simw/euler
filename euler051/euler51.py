from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import defaultdict, Counter
from itertools import combinations

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

def get_indices(input_string, digit, num):
    indices = []
    last_index = 0
    for i in range(num):
        new_index = input_string.find(digit, last_index)
        indices.append(new_index)
        last_index = new_index + 1
    return indices

def all_combinations(input_list):
    combs = []
    for i in range(1, len(input_list)+1):
        combs = combs + list(combinations(input_list, i))
    return combs

def find_repeating_primes(n_max, n_reps):
    self = {} 
    dd_primes = defaultdict(list)
    self['num_digits'] = 0
    self['res'] = []

    def check_prime(prime):
        prime_string = '{0}'.format(prime)
        if len(prime_string) != self['num_digits']:
            # New length, reset our set of primes
            dd_primes.clear() 
            self['num_digits'] = len(prime_string)

        count = Counter(prime_string)
        for el in count:
            digit = el
            num = count[el]
            indices = get_indices(prime_string, digit, num)
            combs = all_combinations(indices)
            for comb in combs:
                prime_string_index = list(prime_string)
                for i in comb:
                    prime_string_index[i] = '*'
                prime_string_index = ''.join(prime_string_index)
                dd_primes[prime_string_index].append(prime)
        
                if len(dd_primes[prime_string_index]) == n_reps:
                    self['res'] = dd_primes[prime_string_index]
                    return True

    generate_primes(n_max, check_prime)
    return self['res']

def main():
    n = int(1e6)
    reps = 8
    primes = find_repeating_primes(n, reps)

    print(primes)
    print(len(primes))
    if primes:
        print(min(primes))

if __name__ == '__main__':
    main()
    

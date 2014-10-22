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

def check_prime_sums(n_max, min_len):
    primes = []
    prime_sums = {}

    def add_prime(prime):
        primes.append(prime)

    def calc_prime_sums():
        for i, v in enumerate(primes):
            this_sum = 0
            for j in xrange(i, len(primes)):
                this_sum += primes[j]
                if this_sum > n_max:
                    break
                this_len = j - i + 1
                if this_sum in prime_sums:
                    if prime_sums[this_sum] < this_len:
                        prime_sums[this_sum] = this_len
                else:
                    prime_sums[this_sum] = this_len

    generate_primes(n_max, add_prime)
    calc_prime_sums()

    primes_set = set(primes)
    max_len = 0
    res = 0
    for k in prime_sums:
        if prime_sums[k] > max_len:
            if k in primes_set:
                max_len = prime_sums[k] 
                res = k

    return (max_len, res)

def main():
    n_max = 100
    res = check_prime_sums(n_max, 5)
    print(res)
    
    n_max = 1000
    res = check_prime_sums(n_max, 20)
    print(res)

    n_max = 1000000
    res = check_prime_sums(n_max, 30)
    print(res)

if __name__ == '__main__':
    main()
 

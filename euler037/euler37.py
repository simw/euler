from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

def generate_primes(n_max, callback_fn):
    numbers = [i for i in range(0, n_max)]

    i = 2
    try:
        while 1:
            num = 0
            # Get next prime number from the list
            while num == 0:
                num = numbers[i]
                i = i + 1

            # Remove all multiples of this prime from the remaining list
            j = 2
            mult = num * j
            while mult < n_max:
                numbers[mult] = 0
                j = j + 1
                mult = num * j

            # Process this prime number
            callback_fn(num)

    except IndexError as e:
        pass

class TruncatableChecker(object):
    def __init__(self):
        self.left_truncatables = [2,3,5,7]
        self.right_truncatables = [2,3,5,7]
        self.both_truncatables = []

    def check_truncatable(self, prime):
        # Must be called in order for every prime
        prime_string = '{0}'.format(prime)
        if len(prime_string) == 1:
            return False

        lstring = int(prime_string[:-1])
        rstring = int(prime_string[1:])

        ltruncable = False
        rtruncable = False
        if lstring in self.left_truncatables:
            ltruncable = True
            self.left_truncatables.append(prime)

        if rstring in self.right_truncatables:
            rtruncable = True
            self.right_truncatables.append(prime)

        if ltruncable and rtruncable:
            self.both_truncatables.append(prime)
            return True

        return False

    def get_truncatables(self):
        return self.both_truncatables

def generate_truncatable_primes(n_max):
    tc = TruncatableChecker()
    generate_primes(n_max, tc.check_truncatable)
    return tc.get_truncatables()

def main():
    truncs = generate_truncatable_primes(1000000)
    print(truncs)
    print(len(truncs))
    print(sum(truncs))

if __name__ == '__main__':
    main()

from __future__ import division
from __future__ import print_function

def next_collatz(x):
    if x % 2 == 0:
        return int(x / 2)
    else:
        return 3 * x + 1

def cache_it(fn):
    cached = {}
    def cached_fn(num):
        if num in cached:
            return cached[num]
        else:
            res = fn(num)
            cached[num] = res
            return res 
   
    return cached_fn

@cache_it
def calc_collatz_len(num):
    if num == 1:
        return 1

    next_num = next_collatz(num)
    return calc_collatz_len(next_num) + 1 

def main():
    max_res = 0 
    for i in range(1, int(1e6)):
        res = calc_collatz_len(i)
        if max_res < res:
            max_i = i
            max_res = res

    print('Max = {0} at {1}'.format(max_res, max_i))

if __name__ == '__main__':
    main()

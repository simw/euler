#!/usr/bin/python

def is_multiple(num, divs):
    for div in divs:
        if num % div == 0:
            return True
    return False

def multiples(max_number, divs):
    return [i for i in range(max_number+1) if is_multiple(i, divs)]

def sum_multiples(max_number, divs):
    nums = multiples(max_number, divs)
    return reduce(lambda x, y: x+y, nums)

if __name__ == '__main__':
    max_number = 1000
    divs = [3, 5]
    print(sum_multiples(max_number, divs))

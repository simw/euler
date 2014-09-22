from __future__ import division

from math import sqrt

def count_divisors(num):
    sqrt_num = int(sqrt(num))
    total = 0
    for i in range(1, sqrt_num):
        if num % i == 0:
            if num == sqrt_num:
                total = total + 1
            else:
                total = total + 2

    return total

def main():
    num = 0
    count = 0
    while 1:
        count = count + 1
        num = num + count
        if count_divisors(num) > 500:
            print(num)
            break
        
if __name__ == '__main__':
    main()

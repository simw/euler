
from math import factorial

def digit_fns(n, fn):
    i = 10
    while i < n:
        nums = [int(n) for n in str(i)]
        sum_fns = sum([fn(n) for n in nums])
        if sum_fns == i:
            yield i
        i = i + 1

def main():
    # Max digits to look at?
    # Compare n*fn(9) with 10^n
    # Assuming that fn(9) is less than exponential

    fn = factorial
    # fn = lambda x: x**5

    nmax = -1
    for n in range(1,20):
        if n*fn(9) < 10**n:
            nmax = n
            break

    if nmax == -1:
        print("Couldn't find nmax")
        exit()
    else:
        print('Max digits = {}, max number = {}'.format(
            nmax, nmax*fn(9))) 

    res = []
    for i in digit_fns(nmax*fn(9)+1, fn):
        print(i)
        res.append(i)

    print('Sum = {}'.format(sum(res)))

if __name__ == '__main__':
    main()

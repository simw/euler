from __future__ import division

def proper_divisors(n_max):
    res = [[] for i in range(0, n_max+1)]

    for i in range(1, n_max+1, 1):
        for j in range(i, n_max+1, 1):
            if i*j > n_max:
                break
            if i > 1 or j > 1:
                res[i*j].append(i)
            if i != j and i > 1:
                res[i*j].append(j)

    return res

def main():
    max_n = 10000 

    divs = proper_divisors(max_n)
    sums = [sum(l) for l in divs]

    amicables = [i for i in range(0, max_n+1) if sums[i] < max_n and sums[sums[i]] == i and sums[i] != i]

    print(amicables)
    print(sum(amicables))

if __name__ == '__main__':
    main()



def integer_triangles(p):
    # i = longest side (ie hypoteneuse)
    # j = next
    # k = shortest (= p - i - j)

    # j must be less than i
    # k must be less than j
    # k must be greater than 1
    # ie j < i and (p-i-j) < j and (p-i-j) > 1
    # ie j < i and j > 0.5*(p-i) and j < (p-i-1)
    
    for i in range(int(p/3), p):
        for j in range(int(0.5*(p-i)), min(i, p-i-1)):
            k = p - i - j
            if i**2 == j**2 + k**2:
                yield (k, j, i)

def main():
    p_max = 0
    n_max = 0
    for p in range(1000):
        res = list(integer_triangles(p))
        if len(res) > n_max:
            p_max = p
            n_max = len(res)
            print('New max: p={}, n={}'.format(p_max, n_max))

if __name__ == '__main__':
    main()

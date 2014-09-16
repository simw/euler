from math import sqrt

def get_triplet(a, b):
    c = sqrt(a**2 + b**2)
    if float(int(c)) == c:
        return int(c)
    else:
        return 0

def generate_triplets(c_max):
    res = []
    for a in range(1, c_max):
        for b in range(a, c_max):
            c = get_triplet(a, b)
            if c != 0:
                res.append((a, b, c))
    return res

def main():
    res = generate_triplets(1000)
    print(res)

    for triplet in res:
        if triplet[0] + triplet[1] + triplet[2] == 1000:
            print(triplet)
            print(triplet[0]*triplet[1]*triplet[2])

if __name__ == '__main__':
    main()

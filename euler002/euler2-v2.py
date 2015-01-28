
def fibber(n):
    fibs = [0, 1]
    i = 0
    while fibs[i] < n:
        yield fibs[i]
        fibs[i] += fibs[~i]
        i = ~i

def sum_even_fibs(n):
    tot = 0
    for f in fibber(n):
        if not(f % 2):
            tot += f

    return tot

def main():
    print(sum_even_fibs(int(4e6)))

if __name__ == '__main__':
    main()

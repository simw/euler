
def fib(n):
    if n == 1 or n == 2:
        return 1

    n1 = 1
    n2 = 1
    i = 0
    while i < n-2:
        res = n1 + n2
        n1 = n2
        n2 = res
        i = i + 1
        print('{0}: {1}'.format(i+2, len('{0}'.format(res))))

    return res

def main(count):
    res = fib(count)

if __name__ == '__main__':
    main(4782)

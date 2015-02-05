
def digit_fifths(n, e):
    i = 10
    while i < n:
        nums = [int(n) for n in str(i)]
        sum_pows = sum([n**e for n in nums])
        if sum_pows == i:
            yield i
        i = i + 1

def main():
    e = 5
    print('Max: n * 9^e = 10^n')
    print('n = 5, {0} = {1}'.format(5 * 9**e, 10**5))
    print('n = 6, {0} = {1}'.format(6 * 9**e, 10**6))

    res = []
    for i in digit_fifths(6*9**e, e):
        print(i)
        res.append(i)

    print('Sum = {}'.format(sum(res)))

if __name__ == '__main__':
    main()

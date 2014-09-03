
divisors = {
    100: 'hundred',
    1000: 'thousand'
}

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def to_words(num, inc_one=True):
    if num in words:
        return words[num]

    if num in divisors:
        if inc_one:
            return '{0} {1}'.format(to_words(1), divisors[num])
        else:
            return '{0}'.format(divisors[num])

    if num <= 100:
        num1 = int(num / 10) * 10
        num2 = num % 10

        return '{0}-{1}'.format(to_words(num1), to_words(num2))

    if num <= 1000:
        num1 = int(num / 100)
        num2 = num % 100

        if num2 == 0:
            return '{0} {1}'.format(to_words(num1), to_words(100, False))
        else:
            return '{0} {1} and {2}'.format(to_words(num1), to_words(100, False), to_words(num2))

if __name__ == '__main__':
    res = 0
    for i in range(1, 1001):
        s = to_words(i)
        print(s)
        s = s.replace('-', '')
        s = s.replace(' ', '')
        res = res + len(s)

    print(res)

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import sys
from io import open

def import_file(filename):
    data = []
    f = open(filename, 'r')

    for line in f:
        data.append(line.strip())

    return data

def extract_nums(data, length):
    nums = []
    for datum in data:
        if datum:
            nums.append(int(datum[:length])) 
    return nums

def main(filename):
    data = import_file(filename)
    nums = extract_nums(data, 13)
    
    total = 0
    for num in nums:
        total = total + num

    print(len(nums))
    print(total)
    print('{0}'.format(total)[:10])

if __name__ == '__main__':
    main(sys.argv[1])


from __future__ import unicode_literals

from io import open


def to_number(name):
    return sum([ord(c)-96 for c in name.lower()])

def get_number(names):
    for name in names:
        name = to_number(name)

    total = 0
    for i, name in enumerate(names):
        total += (i+1) * name

    return total

def get_names():
    names = []
    with open('names.txt', 'r') as f:
        tmp = f.read()
    names = [name.strip('"') for name in tmp.split(',')]
    return names


def main():
    names = get_names()
    names.sort()
    names = [to_number(name) for name in names]
   
    total = 0
    for i, num in enumerate(names):
        total += (i+1) * num
    print(total)

if __name__ == '__main__':
    main()

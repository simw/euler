#!/usr/bin/python

def main():
    nmax = 1000
    
    n3 = int((nmax-0.1) / 3)
    n5 = int((nmax-0.1) / 5)
    n15 = int((nmax-0.1) / 15)
    
    print 3 * sum(range(1, n3+1)) + 5 * sum(range(1, n5+1)) - 15 * sum(range(1,n15+1))

if __name__ == '__main__':
    main()
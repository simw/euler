
class TruncatedNumber(object):
    def __init__(self, n, max_n):
        self.n = n
        self.max_n = max_n

    def truncate(self):
        if self.n > self.max_n:
            self.n = self.n % self.max_n

    def set(self, n):
        self.n = n
        self.truncate()

    def add(self, n):
        self.n = self.n + n
        self.truncate()

    def mult(self, n):
        self.n = self.n * n
        self.truncate()

def main():
    max_n = int(1e11)
    tn = TruncatedNumber(0, max_n)

    tn.set(28433)
    for i in xrange(7830457):
        tn.mult(2)

    tn.add(1)

    print(tn.n)
    print('{0}'.format(tn.n)[-10:])

if __name__ == '__main__':
    main()


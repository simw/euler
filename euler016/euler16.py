from __future__ import division
from __future__ import print_function

def number_to_digit_list(num):
    return [int(x) for x in list('{0}'.format(num))]

class PrecisionNumber(object):
    MAX_PRECISION = 1000

    def __init__(self, num, factor):
        self.factor = factor

        self.nums = [0 for i in range(self.MAX_PRECISION)]

        remainder = num
        for i in range(self.MAX_PRECISION):
            self.nums[i] = remainder % factor
            remainder = int(remainder / factor)
            if remainder == 0:
                break

    def mult(self, num):
        for i in range(self.MAX_PRECISION):
            if self.nums[i] != 0:
                self.nums[i] = self.nums[i] * num

        for i in range(self.MAX_PRECISION):
            if self.nums[i] >= self.factor and i < self.MAX_PRECISION-1:
                self.nums[i+1] = self.nums[i+1] + int(self.nums[i] / self.factor)
                self.nums[i] = self.nums[i] % self.factor
                

    def print_num(self):
        for i in reversed(range(len(self.nums))):
            if self.nums[i] != 0:
                print('{0} x {1}^{2}'.format(self.nums[i], self.factor, i))

    def get_sum_digits(self):
        total = 0
        for i in range(len(self.nums)):
            total = total + sum(number_to_digit_list(self.nums[i]))

        return total

def main():
    # Method 1: using precisionumber class as above
    pn = PrecisionNumber(1, 1000)
    
    for i in range(1000):
        pn.mult(2)

    print('Sum digits = {0}'.format(pn.get_sum_digits()))

    # Method 2: python is clever enough to do this for us ...
    n = 2**1000
    print('Sum digits v2 = {0}'.format(sum(number_to_digit_list(n))))

if __name__ == '__main__':
    main()


class MyDate(object):
    def __init__(self, day, month, year):
        # No error checking here
        self.day = day
        self.month = month
        self.year = year

    def add_days(self, n):
        # Only works for small n
        self.day = self.day + n

        if self.month in [9, 4, 6, 11]:
            days_in_month = 30
        elif self.month == 2:
            if self.year % 4 == 0 and (self.year % 100 !=0 
                    or self.year % 400 == 0):
                days_in_month = 29
            else:
                days_in_month = 28
        else:
            days_in_month = 31

        if self.day > days_in_month:
            self.day = self.day - days_in_month
            self.month = self.month + 1

        if self.month > 12:
            self.month = self.month - 12
            self.year = self.year + 1

def main():
    # Start on 1 Jan 1900, Monday
    d = MyDate(1, 1, 1900)

    # Move to the first Sunday
    d.add_days(6)

    # Now iterate through Sundays to check for 1st of the month
    total = 0
    while 1:
        d.add_days(7)
        if d.day == 1 and d.year >= 1901:
            total = total + 1

        if d.year > 2000:
            break

    print(total)

if __name__ == '__main__':
    main()

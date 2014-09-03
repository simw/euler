
coins = [1, 2, 5, 10, 20, 50, 100, 200]

def counter(total, max_coin=200):
    if max_coin == 1:
        return 1

    count = 0
    for coin in (c for c in coins if c <= max_coin):
        new_total = total - coin

        if new_total < 0:
            pass

        elif new_total == 0:
            count = count + 1

        else:
            count = count + counter(new_total, coin)

    return count 

if __name__ == '__main__':
    print(counter(200))

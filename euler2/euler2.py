import timeit

def fib(n, n_minus1 = 0):
    return n + n_minus1

def fibonacci(n, max_fib = -1):
    previous_result = 1
    result = 1
    temp_result = 0
    results = [previous_result, result]
    
    for i in range(1,n):
        temp_result = result
        result = fib(result, previous_result)
        if result > max_fib:
            break
        previous_result = temp_result
        # print(result)
        results.append(result)
        
    return results

def only_if_even(a):
    if a % 2 == 0:
        return a
    else:
        return 0

def main():
    fibs = fibonacci(100, 4e6)
    fibs = map(only_if_even, fibs)
    print sum(fibs)
    
if __name__ == '__main__':
    # timeit.timeit("main()", number=1);
    main();


nextfib <- function(fibs) {
    tmp = fibs[2]
    fibs[2] = fibs[1] + fibs[2]
    fibs[1] = tmp
    return(fibs)
}

total <- 0
fib = c(0, 1)
repeat {
    if (!(fib[2] %% 2)) {
        total = total + fib[2]
    }
    fib = nextfib(fib) 
    if (fib[2] > 4e6) break
}

print(total)


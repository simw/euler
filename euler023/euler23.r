
divisors <- function(x) {
  sqr <- sqrt(x)
  divs <- seq(1, sqr)
  divs <- divs[x %% divs == 0]
  inv_divs <- x / divs
  divs <- c(divs, (x / divs)[-1])
  if (sqr %% 1 == 0) divs <- divs[-length(divs)]
  return(divs)
}

is_abundant <- function(x) {
  sum(divisors(x)) > x
}

abundants <- function(x_max) {
  purrr::keep(seq(1, x_max), is_abundant) 
}

main <- function(n_max = 28123) {
  print('Calculating abundants ...')
  print(system.time({
    abs <- abundants(n_max)
  }))

  print('Removing sums ...')
  print(system.time({
    vals <- seq(1, n_max)

    l <- length(abs)
    sums <- c(kronecker(rep(1, l), t(abs)) + kronecker(abs, t(rep(1, l))))
    sums <- sums[sums <= n_max]
    vals[sums] <- 0
  }))

  print('Done.')
  print(sum(vals))
}

get_digits <- function(digits, nth_perm) {
  if (nth_perm == 1) return(paste(digits, collapse = ''))
  if (nth_perm < 1) stop(paste0('Error with ', paste(digits, collapse = ', '),
                                ' and nth_perm = ', nth_perm))

  n_digits <- length(digits)
  fact <- factorial(n_digits - 1)
  i <- (nth_perm - 1) %/% fact + 1
  remaining <- nth_perm - (i - 1) * fact

  print(digits[i])
  paste0(digits[i], get_digits(digits[-i], remaining))
}

main <- function(n_digits = 10, nth_perm = 1e6) {
  get_digits(seq(0, n_digits - 1), nth_perm)
}

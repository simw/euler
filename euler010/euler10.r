val_max <- 2e6
vals <- seq(1, val_max)

vals[1] <- 0
for (i in seq(2, val_max / 2)) {
  if (vals[i] > 0) {
    vals[seq(2 * vals[i], val_max, vals[i])] <- 0
  }
}

print(sum(vals))

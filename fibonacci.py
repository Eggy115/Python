start = 1
previous = 0
for counter in range(20):
  fib = start + previous
  print(fib)
  start = previous
  previous = fib

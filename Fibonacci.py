# This function will calculate the fibonacci sequence into its numbers, this is python.
def fib(n):
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()
  
  fib(369)

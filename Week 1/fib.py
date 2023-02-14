def fib(num):
  if num <= 1:
    return num
  else:
    print(f"{num-1} + {num-2} = {num-1+num-2}")
    return(fib(num-1) + fib(num-2))


print(fib(5))

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
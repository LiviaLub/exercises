def fibonacci(num):
  a = 0
  b = 1
  for x in range(0, num):
    if x<= 1:
      c = x
    else:
      c = a + b
      a = b
      b = c

    print (c)

fibonacci(1000)

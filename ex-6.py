def is_armstrong(num):
  result = 0
  temp = num
  while num > 0:
    remainder = num % 10
    num = num // 10
    result = result + (remainder*remainder*remainder)
    
  if result == temp:
    return True
  else:
    return False
  
x = int(raw_input("Enter a number:"))
if is_armstrong(x):
  print("It's Armstrong")
else:
  print("It's not Armstrong")


def isPalindrome(n):
  num = n
  res = 0
  while n>0:
    d = n%10
    n = n//10
    res = res*10 +d
  if num == res:
    return True
  else:
    return False

x = int(raw_input("Enter number:"))
if isPalindrome(x):
  print("It's palindrome")
else:
  print("It's not palindrome")

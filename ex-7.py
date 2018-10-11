def reverse(a):
    res = ""
    l = len(a) - 1
    while l >= 0:
        res = res + a[l]
        l -= 1
    return res
  
print reverse("Hello World")

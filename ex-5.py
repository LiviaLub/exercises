def sort(lst):
  for i in range(1,len(lst)):
    curr = lst[i]
    prev = i - 1
    while prev >= 0:
      if curr < lst[prev]:
        lst[prev + 1] = lst[prev]
        lst[prev] = curr
        prev -= 1
      
      else:
        break
    return lst
a = [7,1,3,5,2,9]
print(sort(a))

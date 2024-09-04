def func1(arr):
  if len(arr) != 0:
    if arr[0] == arr[-1]:
      return True
  return False


print(func1([1,2,3,4])) 
print(func1([1,2,3,4,1]))
print(func1([]))

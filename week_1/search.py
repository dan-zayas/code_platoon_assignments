def linear_search(obj, arr):
  for i in arr:
    if arr[i] == obj:
      return i
  return None


def global_linear_search(obj, arr):
  newArr = []
  i = 0
  while i < len(arr):
    if arr[i] == obj:
      newArr.append(i)
    i += 1
      
  
  return newArr

print(linear_search(3, [1,2,3,4,5,6,7]))
bananas_list = list('bananas')

print(global_linear_search("a", bananas_list))
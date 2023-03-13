# 재귀
def binary_search(array, target, start, end):

  if start > end:
    return None
  mid = (start+end) // 2
  if array[target] == array[mid]:
    return mid
  elif array[target] > array[mid]:
    return binary_search(array, target, mid+1, end)
  else :
    return binary_search(array, target, start, mid-1)

# 반복문
def binary_search(array, target, start, end):

  while start <= end:
    mid = (start+end) // 2
    if array[target] == array[mid]:
      return mid
    elif array[target] > array[mid]:
      start = mid+1
    else :
      end = mid-1
    return None

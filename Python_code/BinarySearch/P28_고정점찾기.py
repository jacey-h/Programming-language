n = int(input())
array = list(map(int,input().split()))

start = 0
end = len(array)-1
answer = None
while start <= end:
  mid = (start + end) // 2

  if mid == array[mid]:
    answer = mid
    break
  elif mid > array[mid]:
    start = mid + 1
  else:
    end = mid - 1

if answer == None:
  print(-1)
else:
  print(answer)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_data = i
  for j in range(i+1,len(array)):
    if array[min_data] > array[j]:
      min_data = j
  array[i], array[min_data] = array[min_data], array[i]

print(array)
    
    
    
    
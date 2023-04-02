n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  array.append((input_data[0],int(input_data[1]),int(input_data[2]),int(input_data[3])))

# 강력한 sort 함수 특징 파악하기
array.sort(key = lambda score : (-score[1], score[2], -score[3], score[0]))


for student in array:
  print(student[0])
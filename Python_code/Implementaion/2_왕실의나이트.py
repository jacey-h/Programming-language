location = input()
x,y=ord(location[0]),int(location[1])
move_types = ['R','L','U','D']
dx = [+1,-1,0,0]
dy = [0,0,-1,+1]
move_directions = ['RRU','RRD','LLU','LLD','UUR','UUL','DDR','DDL']
count =0 
for direction in move_directions:
  for j in range(3):
    for i in range(len(move_types)):
      if move_types[i] == direction[j]:
        nx = x + dx[i]
        ny = y + dy[i]
        x,y = nx,ny

  if (x<ord('a') or x>ord('h') or y<1 or y>8)==False:
    count+=1
  x,y=ord(location[0]),int(location[1])

print(count)

# 정답
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])-int(ord('a')))+1

steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if 1<= next_row <=8 and 1<= next_column <=8:
        result +=1
print(result)
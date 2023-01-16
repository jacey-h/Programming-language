# n,m = map(int,input().split())
# a,b,d = map(int,input().split())

# maps = [[0]*n for _ in range(m)]
# for i in range(n):
#   maps[i]=list(map(int,input().split()))

# d_tape = [0,1,2,3]
# db = [0,1,0,-1]
# da = [-1,0,1,0]
# b,a = b,a
# maps[a][b] = 2
# count = 0
# cnt = 0
# num=0
# print(maps[0][0])
# print(maps[1][1])
# print(maps[1][2])
# print(f'전 b,a ={b,a}')
# while True:
#   nb,na = 0,0
#   for i in range(len(d_tape)):
#     if d == d_tape[i]:
#       d_left = d_tape[i-1]
#   nb = b + db[d_left]
#   na = a + da[d_left]
#   print(f'test nb,na ={nb,na}')
#   print(maps[a][b])
#   print(f'1번 b,a ={b,a}')
#   if maps[na][nb] == 0:
#     d = d_left
#     print(f'1번 d ={d}')
#     print(f'1번 nb,na ={nb,na}')
#     b,a = nb,na
#     maps[a][b] = 2
#     count += 1
#     print(f'count ={count}')
#   else:
#     d = d_left
#     print(f'2 번 d ={d}')
#   print(maps[a][b])
#   print(f'2번 b,a ={b,a}')
#   if num == 10:
#     break
#   for j in range(len(d_tape)):
#     nb = b + db[i]
#     na = a + da[i]
#     if (maps[na][nb] == 1) or (maps[na][nb] == 2):
#       cnt +=1
#   if cnt == 4:
#     nb = b + db[d-2]
#     na = a + da[d-2]
#     b,a = nb,na    
#     if maps[na][nb] == 1:
#       break
#   num += 1



# print(count)

n,m = map(int,input().split())
a,b,d = map(int,input().split())

maps = [[0]*n for _ in range(m)]
for i in range(n):
  maps[i]=list(map(int,input().split()))

d_type = [0,1,2,3]
db = [0,1,0,-1]
da = [-1,0,1,0]
maps[a][b] = 2
count = 1
cnt = 0

while True:
  na,nb = 0,0
  cnt =0
  for i in range(len(d_type)):
    if d == d_type[i]:
      d_left = d_type[i-1]
  na = a + da[d_left]
  nb = b + db[d_left]
  print(f'test na,nb ={na,nb}')
  print(f'1번 a,b ={a,b}')
  if maps[na][nb] == 0:
    d = d_left
    print(f'1번 d ={d}')
    print(f'test na,nb ={na,nb}')
    b,a = nb,na
    maps[a][b] = 2
    count += 1
    print(f'count ={count}')
  else:
    d = d_left
  for j in range(len(d_type)):
    nb = b + db[j]
    na = a + da[j]
    if (maps[na][nb] == 1) or (maps[na][nb] == 2):
      cnt +=1
      print(f'cnt ={cnt}')
  if cnt == 4:
    nb = b + db[d-2]
    na = a + da[d-2]
    print(f'st na,nb ={na,nb}')

    b,a = nb,na  
    print(f'count ={count}')

    if maps[na][nb] == 1:
      break

print(count)
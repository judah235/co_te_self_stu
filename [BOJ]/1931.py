import sys
input=sys.stdin.readline

n=int(input())

l_l=[]
for _ in range(n):
  l_l.append(list(map(int,input().split())))

l_l.sort(key=lambda x:x[0])
l_l.sort(key=lambda x:x[1])

cnt=1
e_t=l_l[0][1]

for i in range(1,n):
  if l_l[i][0]>=e_t:
    cnt+=1
    e_t=l_l[i][1]
print(cnt)
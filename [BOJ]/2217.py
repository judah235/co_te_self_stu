import sys
input=sys.stdin.readline

k=int(input())

k_l=[]
for _ in range(k):
    k_l.append(int(input()))
k_l.sort()
ans=[]

for i in range(k):
    ans.append(k_l[i]*(k-i))
print(max(ans))
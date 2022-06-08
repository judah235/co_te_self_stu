import sys
input=sys.stdin.readline

n,m=map(int,input().split())
s={}
for _ in range(n):
    s[input()]=0

ans=0
for _ in range(m):
    if input() in s:
        ans+=1
print(ans)
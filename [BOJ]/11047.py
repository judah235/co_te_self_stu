import sys
input=sys.stdin.readline

n, k =map(int,input().split())

a_l=[int(input()) for _ in range(n)]

ans=0
for i in a_l[::-1]:
    if k>=i:
        ans+=k//i
        k=k%i
print(ans)
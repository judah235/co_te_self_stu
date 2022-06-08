import sys
input=sys.stdin.readline


input()
n=list(map(int,input().split()))

n_d={}
for i in n:
    if not i in n_d:
        n_d[i]=0
    n_d[i]+=1

input()
print(*[n_d[i] if i in n_d else 0 for i in map(int,input().split())])
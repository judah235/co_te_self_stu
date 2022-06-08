import sys
input=sys.stdin.readline

n,m=map(int,input().split())
듣잡={}
듣보잡=[]
for i in range(n):
    듣잡[input().rstrip()]=0
for i in range(m):
    보잡=input().rstrip()
    if (듣잡.setdefault(보잡,1))==0:
        듣보잡.append(보잡)
듣보잡.sort()
print(len(듣보잡))
print(*듣보잡, sep='\n')
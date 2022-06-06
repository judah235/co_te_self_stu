import sys
input=sys.stdin.readline

n=int(input())

n_l=[]
for _ in range(n):
  n_l.append(int(input()))
n_l.sort()
print(*n_l,sep='\n')
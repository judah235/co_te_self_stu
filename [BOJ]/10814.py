import sys

input = sys.stdin.readline

n = int(input())

n_l=[]
for _ in range(n):
    i=input().split()
    n_l.append([int(i[0]),i[1]])
n_l=sorted(n_l, key=lambda x:x[0])
for i in n_l:
    print(*i,sep=' ')
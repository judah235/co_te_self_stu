import sys
input=sys.stdin.readline

n=int(input())

d_l=[]
for _ in range(n):
    d_l.append(list(map(int, input().split())))
d_l.sort()
for i in d_l:
    print(*i)
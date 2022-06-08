import sys
input=sys.stdin.readline

n=int(input())

d_l=[]
for _ in range(n):
    d_l.append(list(map(int, input().split())))
for i in d_l:
    i.reverse()
d_l.sort()
for i in d_l:
    i.reverse()
    print(*i)
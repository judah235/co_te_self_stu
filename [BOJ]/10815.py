import sys
input=sys.stdin.readline

input()
n_d={i:0 for i in map(int,input().split())}
input()
print(*[1 if i in n_d else 0 for i in map(int,input().split())])
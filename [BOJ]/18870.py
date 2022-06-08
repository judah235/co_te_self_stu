import sys

input = sys.stdin.readline

input()

n_l=list(map(int, input().split()))
n_l2=sorted(set(n_l))

n_d={n:i for i,n in enumerate(n_l2)}

for i in n_l:
    print(n_d[i],end=' ')
import sys

input=sys.stdin.readline

n=int(input())

n_l=[0]*10001

for _ in range(n):
  n_l[(int(input()))]+=1
      
for i,n in enumerate(n_l):
  if n!=0:
    for _ in range(n):
      print(i)
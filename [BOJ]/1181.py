import sys
input=sys.stdin.readline

n=int(input())

d={}
for _ in range(n):
    i=input()
    d[i]=len(i)
        
s_d=sorted(d.items(), key=lambda x : (x[1],x[0]))
for i in s_d:
    print(i[0],end='')
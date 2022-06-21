import sys
input=sys.stdin.readline

n,m=map(int,input().split())

one=1001
six=1001
for i in range(m):
    s, o=map(int,input().split())
    if one>o:
        one=o
    if six>s:
        six=s
if one*6<=six:
    print(n*one)
else:
    if n//6*six+n%6*one < (n//6+1)*six:
        print(n//6*six+n%6*one)
    else:
        print((n//6+1)*six)
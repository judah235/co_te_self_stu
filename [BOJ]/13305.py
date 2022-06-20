import sys
input=sys.stdin.readline

n=int(input())
city_l=list(map(int,input().split()))
oil_p=list(map(int,input().split()))
pay=0
for i in range(n-1):
    if i==0:
        p=oil_p[i]
    elif p>oil_p[i]:
        p=oil_p[i]
    pay+=p*city_l[i]
print(pay)
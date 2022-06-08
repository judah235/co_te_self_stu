import sys

n,m=map(int,(input().split()))
pok_name={}
pok_num={}
for i in range(1,n+1):
    p_n=sys.stdin.readline().rstrip()
    pok_name[p_n]=i
    pok_num[str(i)]=p_n
for i in range(m):
     q= sys.stdin.readline().rstrip()
     print(pok_name.get(q,''),pok_num.get(q,''),sep='')
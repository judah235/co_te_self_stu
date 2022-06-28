import sys
input=sys.stdin.readline

n, l =map(int,input().split())
f_l=list(map(int,input().split()))
f_l.sort()

ans=0
while True:
    a=f_l[0]
    ans+=1
    for i in f_l[:]:
        if i>a+l-1:
            break
        else:
            f_l.remove(i)
    else:
        break
print(ans)
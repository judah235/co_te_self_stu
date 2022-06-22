import sys
input=sys.stdin.readline

n,m = map(int,input().split())

a = [list(input().strip()) for _ in range(n)]
b = [list(input().strip()) for _ in range(n)]

ans=0
for y in range(0,n-2):
    for x in range(0,m-2):
        if a[y][x]!=b[y][x]:
            ans+=1
            for y_2 in range(y,y+3):
                for x_2 in range(x,x+3):
                    if a[y_2][x_2]=='0':
                        a[y_2][x_2]='1'
                    else:
                        a[y_2][x_2] = '0'
if a==b:
    print(ans)
else:
    print(-1)
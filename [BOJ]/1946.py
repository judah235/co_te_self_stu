import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n = int(input())
    t_l=[list(map(int,input().split())) for _ in range(n)]
    t_l.sort(key=lambda x:x[0])
    p_t=t_l[0][1]
    ans=1
    for i in t_l:
      if i[1]<p_t:
        ans+=1
        p_t=i[1]
    print(ans)
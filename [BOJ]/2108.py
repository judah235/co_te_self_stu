import sys
input=sys.stdin.readline

n=int(input())

n_l=[]
n_d={}
for _ in range(n):
    i=int(input())
    n_l.append(i)
    if not i in n_d:
        n_d[i]=0
    n_d[i]+=1

n_l.sort()
print(round(sum(n_l)/n))

print(n_l[(n-1)//2])

m_f=max(n_d.values())
m_f_v=[k for k,v in n_d.items() if v==m_f]
m_f_v.sort()
print(m_f_v[0] if len(m_f_v)==1 else m_f_v[1])

print(max(n_l)-min(n_l))
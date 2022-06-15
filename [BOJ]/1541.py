import re
r=re.compile('[^0-9]')

eq=input()
n_l=r.split(eq)
op_l=r.findall(eq)

n_l=list(map(str,(map(int,n_l))))

eq=n_l[0]
for i in range(len(n_l)-1):
    eq += op_l[i]
    eq+=n_l[i+1]


eq=eq.split('-')
if len(eq)==1:
    print(eval(eq[0]))
else:
    ans = eval(eq[0])
    for i in range(1,len(eq)):
        ans-=eval(eq[i])
    print(ans)
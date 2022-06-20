a,b=map(int,input().split())

b_l=[b]

while b%2==0 or str(b)[-1]=='1':    
    if b==1:
        print(-1)
        break
    elif b%2==0:
        b=int(b//2)
        b_l.append(b)
        if b==a:
            print(len(b_l))
            break
    elif str(b)[-1]=='1':
        b=int(str(b)[:-1])
        b_l.append(b)
        if b==a:
            print(len(b_l))
            break
else:
    print(-1)
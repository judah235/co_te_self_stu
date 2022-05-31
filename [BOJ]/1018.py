m,n=map(int,input().split())

bord=[input() for _ in range(m)]

answer=[]
for y in range(m-7):
    for x in range(n-7):
        w_f = 0
        b_f = 0
        for i in range(y,y+8):
            for j in range(x,x+8):
                if (i+j)%2==0:
                    if bord[i][j]=='W':
                        b_f+=1
                    else:
                        w_f+=1
                else:
                    if bord[i][j] == 'W':
                        w_f += 1
                    else:
                        b_f += 1
        answer.append(w_f if w_f <b_f else b_f)
print(min(answer))
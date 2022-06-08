s=input()
s_l=len(s)

s_lis=[]
for i in range(s_l):
  s_lis.append(s[i])
  n=2
  while True:
    if i+n<=s_l:
      s_lis.append(s[i:i+n])
    else:
        break
    n+=1
print(len(set(s_lis)))
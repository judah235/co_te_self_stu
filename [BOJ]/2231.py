n=input()
n_l=len(n)
n=int(n)

m_max=n_l*9
m_min=n-m_max if n-m_max >=0 else 0

for i in range(m_min,n):
  m=0
  j=i
  while j!=0:
    m+=j%10
    j=j//10
  if m+i==n:
    print(i)
    break
else:
  print(0)
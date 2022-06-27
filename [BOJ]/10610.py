n=[int(i) for i in input()]

if not 0 in n:
  print(-1)
elif sum(n)%3==0:
  n.sort(reverse=True)
  n=list(map(str,n))
  n=int(''.join(n))
  print(n)
else:
  print(-1)
dst=[]
a=666
n=int(input())
while True:
  if '666' in str(a):
    dst.append(a)
  if len(dst)==n:
    break
  a+=1

print(dst[-1])
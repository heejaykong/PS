T=int(input())
for i in range(T):
  temp=[]
  stack=list(input())
  for char in stack:
    if char == '(':
      temp.append(char)
    elif temp and temp[-1]=='(':
        temp.pop()
    else:
        temp.append(char)
  if temp: print('NO')
  else: print('YES')
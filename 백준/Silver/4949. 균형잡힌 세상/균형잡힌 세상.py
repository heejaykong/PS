import sys
while True:
  s = sys.stdin.readline().rstrip()
  if s == '.': break
  temp = []
  flag = True
  for chr in s:
    if chr == '(' or chr == '[':
      temp.append(chr)
    elif chr == ')':
      if temp and temp[-1] == '(':
        temp.pop()
      else:
        flag = False
        break
    elif chr == ']':
      if temp and temp[-1] == '[':
        temp.pop()
      else:
        flag = False
        break
  if flag and not temp: print('yes')
  else: print('no')
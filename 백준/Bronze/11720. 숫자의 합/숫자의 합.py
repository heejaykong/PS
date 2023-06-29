T = int(input())
numbers = list(input())
if len(numbers) != T:
  exit()
print(sum(map(int, numbers)))
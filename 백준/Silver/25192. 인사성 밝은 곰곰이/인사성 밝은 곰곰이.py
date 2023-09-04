n = int(input())

logs = [input().strip() for i in range(n)]
said_hi = set()
ans = 0
for log in logs:
    if log == "ENTER":
        ans += len(said_hi)
        # print(said_hi)
        said_hi.clear()
    else:
        said_hi.add(log)
ans += len(said_hi)
# print(said_hi)

print(ans)
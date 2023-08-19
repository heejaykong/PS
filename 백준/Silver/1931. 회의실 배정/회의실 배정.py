# 속도차이를 보기위한 남의거 베껴쓰기
import sys
In = sys.stdin.readline

def main():
    n = int(In())
    meetings = [(*map(int, In().split()),) for _ in range(n)]
    meetings.sort()
    n, st = 0, float('inf')
    for m in reversed(meetings):
        if m[1] <= st:
            st = m[0]
            n += 1
    print(n)

main()
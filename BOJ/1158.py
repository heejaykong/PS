# 내 힘으로 푼 코드
N, K = map(int, input().split())
queue = []
result = []
q_index = K-1
# 초기화
for i in range(1,N+1):
    queue.append(str(i))
# 실행
while queue:
    if q_index >= len(queue):
        while q_index >= len(queue):
            q_index -= len(queue)
    result.append(queue.pop(q_index))
    q_index += (K-1)
str=', '.join(result)
print(f'<{str}>')

# 남의 것 참고해서 더 최적화한 코드
N, K = map(int, input().split())
queue = list(range(1,N+1)) #초기화
result = []
q_index = 0 #생각해보니 index를 굳이 K-1로 시작할 필요는 없었음ㅎ
# 실행
while queue:
    q_index = (q_index+(K-1)) % len(queue) #while문 대신 나머지 구하기(%)를 쓰면 될 일이었음
    result.append(str(queue.pop(q_index)))
print('<', ', '.join(r), '>', sep='') #이렇게 출력하는 방법도 있다

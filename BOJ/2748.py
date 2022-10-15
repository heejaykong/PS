#  DP 유형의 기본인 피보나치 수 문제

def solution(nth):
    first, second = 0, 1
    # first, second, temp를 서로 바꿔가며 엉금엉금 앞으로 나아가기(마치 걸어다니는 키네신 세포처럼)
    for _ in range(nth - 1):
        temp = first + second
        first = second
        second = temp
    return second

nth = int(input())
print(solution(nth))

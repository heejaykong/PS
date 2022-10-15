# 삼성 기출 풀어보기

# 총 시험장 개수
n = int(input())
# 각 시험장의 응시자 수
classList = list(map(int, input().split()))
# B(총감독관이 감시가능한 인원수)와 C(부감독관이 감시가능한 인원수)
limits = list(map(int, input().split()))

def solution(n, classList, limits):
    b = limits[0]  # 총감독관
    c = limits[1]  # 부감독관
    answer = 0

    for ppl in classList:
        answer += 1  # 총감독관은 무조건 시험장마다 1명씩은 있어야 한다
        ppl -= b
        if ppl > 0:  # 총감독관이 들어가고 남는 감시대상이 있는지 확인
            secDirCnt = ppl // c  # 필요한 부감독관 인원수
            answer += secDirCnt
            if (ppl % c) > 0:  # 완전히 나누어떨어지지 않는다면 부감독관 한명 더 투입돼야 함
                answer += 1
    print(answer)

solution(n, classList, limits)

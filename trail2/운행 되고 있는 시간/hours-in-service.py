n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
max_operating_time = 0

# i번째 개발자를 해고하는 경우
for i in range(n):
    # 시간대별(1~1000) 일하는 직원 유무 체크
    working_time = [False] * 1001
    
    # i번째 제외 나머지 개발자들의 시간 반영
    for j in range(n):
        if i == j:
            continue
        for t in range(a[j], b[j]):
            working_time[t] = True
            
    # 운행 되고 있는 총 시간 계산
    current_time = sum(working_time)
    max_operating_time = max(max_operating_time, current_time)

print(max_operating_time)
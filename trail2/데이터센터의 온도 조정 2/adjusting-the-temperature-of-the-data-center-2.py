N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
answer = 0

min_temp = float('inf')
max_temp = 0
for t_a,t_b in ranges:
    min_temp = min(min_temp, t_a)
    max_temp = max(max_temp, t_b)

# 전체 범위는 가장 낮은 T_a - 1 부터 가장 높은 T_b + 1
for temperature in range(min_temp-1, max_temp+1+1) :
    workload = 0
    for t_a,t_b in ranges:
        if temperature < t_a:
            workload += C
        elif temperature >= t_a and temperature <= t_b:
            workload += G
        else:
            workload += H
    answer = max(answer,workload)

print(answer)
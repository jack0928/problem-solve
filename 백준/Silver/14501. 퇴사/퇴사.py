'''
DP 느낌
dp[i] = i일까지 얻을 수 있는 최대 수익
dp[i+1] = max(dp[i+1], dp[i]) # i번째 상담을 안 하는 경우
dp[i + T_i] = max(dp[i + T_i], dp[i] + P_i) # i번째 상담을 하는 경우
'''
n = int(input())
schedule = []
dp = [0 for _ in range(n + 1)]
for _ in range(n):
    t,p = map(int, input().split())
    schedule.append((t,p))

for i in range(n):
    # 상담 안 하는 경우
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 상담 하는 경우
    t, p = schedule[i]
    if i + t <= n:
        dp[i + t] = max(dp[i + t], dp[i] + p)

print(dp[n])
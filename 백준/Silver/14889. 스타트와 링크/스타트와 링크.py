# 일단 팀을 나누는 경우의 수는 N_C_(N/2) = N!/((N/2)!) -> N이 최대인 20이면 20C10 ≈ 184,756니까 그냥 하면 됨
from itertools import combinations

def calc(team):
    total = 0
    # 돌아가면서 S_ij 더하는 과정
    for i in team:
        for j in team:
            total += stats[i][j]
    return total

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]

players = range(n)
min_diff = int(1e9)

for team in combinations(players, n//2):
    # 팀 나누기
    team = set(team)
    other = set(players) - team

    diff = abs(calc(team) - calc(other))
    min_diff = min(min_diff, diff)

print(min_diff)
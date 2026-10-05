ability = list(map(int, input().split()))

# Please write your code here.
# 2개 골라 빼면 2팀을 만들 수 있고, 이때 가장 적게 차이가 나게 하려면 1-4, 2-3으로 묶어야 함
from itertools import combinations

answer = 10**15
arr = list(combinations(ability, 2))

for i in range(len(arr)):
    # ability[:]를 사용하여 슬라이싱 복사를 진행
    temp_team = ability[:] 
    temp_team.remove(arr[i][0])
    temp_team.remove(arr[i][1])
    
    temp_team.sort()
    team1 = temp_team[0] + temp_team[3]
    team2 = temp_team[1] + temp_team[2]
    team3 = arr[i][0] + arr[i][1]
    team_list = sorted([team1,team2,team3])
    result = team_list[2] - team_list[0]
    answer = min(answer, result)

print(answer)
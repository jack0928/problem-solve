'''
M이 최대 13이고, M <= 치킨집 개수 <= 13이다.
즉, 남길 치킨 집을 고르는 경우는 최대 13_C_M이다. 따라서 이는 13_C_6 혹은 13_C_7인 1716이다.
남길 치킨집이 정해졌을 때 치킨 거리를 구하는 방법
1.최대 13개의 치킨집과의 거리 직접 비교. O(1).
- N이 최대 50이고, 집은 최대 2N개이므로 100개. 즉 100*13을 해도 1300
=> 1716 * 1300 = 대략 2000 * 1000 = 2,000,000 따라서 1초 언더 (1초가 1억이니까)
'''
from itertools import combinations

# 치킨 거리 계산 함수
def calculate_chicken_distance(house_list, chicken_restaurant_list):
    total_distance = 0 # 이 조합인 도시에서의 최소 치킨 거리
    for house in house_list:
        distance = 10000
        # 해당 집 기준으로 가장 짧은 치킨 거리 찾기
        for restaurant in chicken_restaurant_list:
            distance = min(distance, abs(house[0] - restaurant[0]) + abs(house[1] - restaurant[1]))
        total_distance += distance
    return total_distance

n,m = map(int,input().split())
city = []
houses = []
chickens = []

# 도시 입력
for i in range(n):
    avenue = list(map(int, input().split()))
    city.append(avenue)
    # 집과 치킨집 기록
    for j in range(n):
        if avenue[j] == 1:
            houses.append((i,j))
        elif avenue[j] == 2:
            chickens.append((i,j))

# 가능한 치킨집 조합 확인
possible_combinations = list(combinations(chickens, m))
answer = int(1e9)
# 치킨 거리 계산
for combi in possible_combinations:
    answer = min(answer, calculate_chicken_distance(houses, combi))

print(answer)
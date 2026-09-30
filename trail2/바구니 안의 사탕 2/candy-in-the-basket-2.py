N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
# 투 포인터 (슬라이딩 윈도우)
baskets = []
for i in range(N):
    c, p = candy[i], pos[i]  # c: 사탕 개수, p: 위치
    baskets.append((p, c))            # (위치, 사탕 개수) 형태로 저장

# 1. 위치 기준 정렬
baskets.sort()

max_candies = 0

# 2. 각 바구니를 '구간의 시작점'으로 지정
right = 0
current_sum = 0

for left in range(N):
    # right를 구간의 끝(baskets[left][0] + 2*K) 범위 내까지 확장
    while right < N and baskets[right][0] <= baskets[left][0] + 2 * K:
        current_sum += baskets[right][1]
        right += 1
        
    max_candies = max(max_candies, current_sum)
    
    # left 바구니를 다음 위치로 옮기기 전에 현재 left의 사탕 차감
    current_sum -= baskets[left][1]

print(max_candies)
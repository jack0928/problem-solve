N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
answer = 0

P.sort()

# i번째 물건에 반값 쿠폰을 적용하는 모든 경우 탐색
for i in range(N):
    cnt = 0
    left_budget = B
    
    # 정렬된 물건들을 차례대로 구매
    for j in range(N):
        # i번째 물건은 half 가격 적용, 그 외는 정가 적용
        cost = P[j] * 0.5 if j == i else P[j]
        
        if left_budget >= cost:
            left_budget -= cost
            cnt += 1
        else:
            break  # 예산이 부족하면 종료 (이미 정렬되어 있으므로)
            
    answer = max(answer, cnt)

print(answer)
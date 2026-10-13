N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# (가격 + 배송비) 기준으로 오름차순 정렬
sorted_indices = sorted(range(N), key=lambda x: P[x] + S[x])
max_count = 0

# i번째 선물에 반값 할인을 적용하는 경우를 확인
for i in range(N):
    discount_cost = P[i] // 2 + S[i]
    if discount_cost > B:
        continue
        
    current_b = B - discount_cost
    count = 1  # i번째 선물 구매
    
    # 정렬된 순서대로 저렴한 선물부터 예산 내 구매
    for idx in sorted_indices:
        if idx == i:
            continue  # 이미 할인가로 산 선물은 건너뜀
            
        cost = P[idx] + S[idx]
        if current_b >= cost:
            current_b -= cost
            count += 1
        else:
            break  # 예산 초과 시 즉시 종료
            
    max_count = max(max_count, count)

print(max_count)

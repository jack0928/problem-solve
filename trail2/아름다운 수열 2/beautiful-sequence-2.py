N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
# 아름다운 수열이라 함은 결국 특정 원소가 특정 개수만큼 있다는 뜻
from collections import Counter

# B의 원소 빈도수 계산
target_counter = Counter(B)
# A의 첫 번째 M개 원소 빈도수 계산
window_counter = Counter(A[:M])

answer = 0

# 첫 번째 윈도우 검사
if window_counter == target_counter:
    answer += 1

# 슬라이딩 윈도우 진행 (O(N) 시간 복잡도)
for i in range(1, N - M + 1):
    # 이전 윈도우의 맨 앞 원소 제거
    out_elem = A[i - 1]
    window_counter[out_elem] -= 1
    if window_counter[out_elem] == 0:
        del window_counter[out_elem]
    
    # 새 윈도우의 맨 뒤 원소 추가
    in_elem = A[i + M - 1]
    window_counter[in_elem] += 1
    
    # 빈도수가 일치하는지 확인
    if window_counter == target_counter:
        answer += 1

print(answer)
arr = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations
answer = float('inf')

# 인덱스(0, 1, 2, 3, 4) 기준으로 그룹 분할
for idx1 in combinations(range(5), 2):
    sum1 = sum(arr[i] for i in idx1)
    
    rem_idx1 = [i for i in range(5) if i not in idx1]
    
    for idx2 in combinations(rem_idx1, 2):
        sum2 = sum(arr[i] for i in idx2)
        
        idx3 = [i for i in rem_idx1 if i not in idx2][0]
        sum3 = arr[idx3]
        
        # 조건: 모든 팀의 능력치가 서로 달라야 함
        if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
            continue
        
        diff = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
        answer = min(answer, diff)

# 만족하는 조합이 없는 경우 -1 출력
print(answer if answer != float('inf') else -1)
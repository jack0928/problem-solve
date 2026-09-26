n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 첫 번째 1x3 격자의 위치 (i1, j1)
for i1 in range(n):
    for j1 in range(n - 2):
        sum1 = sum(arr[i1][j1:j1+3])  # j1:j1+3 으로 슬라이싱 수정
        
        # 두 번째 1x3 격자의 위치 (i2, j2)
        for i2 in range(n):
            for j2 in range(n - 2):
                # 1) 같은 행일 때는 두 번째 격자가 첫 번째 격자와 겹치지 않아야 함 (j2 >= j1 + 3)
                # 2) 다른 행일 때는 항상 중복 탐색을 피하기 위해 i2 > i1 조건 사용
                if (i1 == i2 and j2 >= j1 + 3) or (i2 > i1):
                    sum2 = sum(arr[i2][j2:j2+3])
                    answer = max(answer, sum1 + sum2)

print(answer)
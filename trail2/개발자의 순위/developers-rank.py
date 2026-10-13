k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
# 첫번째 배열 기준으로 추가해놓고, 어긋나는 애들마다 탈락시키기

# 첫번째 경기 결과 기준 내 뒤에 오는 애들 정리
under_than_me = [[] for _ in range(n+1)]
for i in range(n):
    num = arr[0][i]
    under_than_me[num] = arr[0][i+1:]

# 나머지 경기 결과 확인하며 탈락
for i in range(1, k):
    for j in range(n):
        num = arr[i][j]
        new_under_than_me = list(set(under_than_me[num]) & set(arr[i][j+1:]))
        under_than_me[num] = new_under_than_me

answer = 0
for i in range(1, n+1):
    answer += len(under_than_me[i])

print(answer)
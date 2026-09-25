N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
answer = 0
# 방향별 읽는 함수 구현
def check_lee(x,y):
    global answer
    # 상
    if i - 2 >= 0 and arr[i-1][j] == 'E' and arr[i-2][j] == 'E':
        answer += 1
    # 하
    if i + 2 < N and arr[i+1][j] == 'E' and arr[i+2][j] == 'E':
        answer += 1
    # 좌
    if j - 2 >=0 and arr[i][j-1] == 'E' and arr[i][j-2] == 'E':
        answer += 1
    # 우
    if j + 2 < M and arr[i][j+1] == 'E' and arr[i][j+2] == 'E':
        answer += 1
    # 45도
    if i - 2 >= 0 and j + 2 < M and arr[i-1][j+1] == 'E' and arr[i-2][j+2] == 'E':
        answer += 1
    # 135도
    if i - 2 >= 0 and j - 2 >= 0 and arr[i-1][j-1] == 'E' and arr[i-2][j-2] == 'E':
        answer += 1
    # 225도
    if i + 2 < N and j - 2 >= 0 and arr[i+1][j-1] == 'E' and arr[i+2][j-2] == 'E':
        answer += 1
    # 315도
    if i + 2 < N and j + 2 < M and arr[i+1][j+1] == 'E' and arr[i+2][j+2] == 'E':
        answer += 1

# 매 'L'마다 8방향 탐색
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            # 8방향 탐색
            check_lee(i,j)

print(answer)
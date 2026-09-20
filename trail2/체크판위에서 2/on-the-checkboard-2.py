R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
answer = 0
first_stop = []

# 첫번째 점프
for i in range(1, R):
    for j in range(1,C):
        if grid[i][j] != grid[0][0] and i < R-2 and j < C-2:
            first_stop.append((i,j)) # 가능한 첫번째 경유지

# 두번째 점프
for x,y in first_stop:
    for i in range(x+1,R):
        for j in range(y+1,C):
            if grid[i][j] != grid[x][y] and grid[i][j] != grid[R-1][C-1] and i < R-1 and j < C-1:
                answer += 1

print(answer)
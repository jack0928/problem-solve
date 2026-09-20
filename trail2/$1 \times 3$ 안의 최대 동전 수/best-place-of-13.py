n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
for i in range(n):
    for j in range(n-2):
        answer = max(answer, sum(grid[i][j:j+3]))

print(answer)
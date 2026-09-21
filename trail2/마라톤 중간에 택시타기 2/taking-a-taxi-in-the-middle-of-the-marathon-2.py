n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
answer = 10**9

for i in range(1, n-1):
    # 하나씩 빼보면서 전체 케이스 테스트
    new_x = x[:i] + x[i+1:]
    new_y = y[:i] + y[i+1:]
    distance = 0
    
    for j in range(n-2):   
        distance += abs(new_x[j] - new_x[j+1]) + abs(new_y[j] - new_y[j+1])

    answer = min(answer, distance)

print(answer)
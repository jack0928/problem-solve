n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
answer = float('inf')
# 있는 점들을 포함하는 최소 직사각형의 넓이를 구하는 함수
def make_rectangle(x,y):
    left, right = min(x), max(x)
    bottom, top = min(y), max(y)
    return ((right - left) * (top - bottom))

for i in range(n):
    temp_x = x[:i] + x[i+1:]
    temp_y = y[:i] + y[i+1:]
    answer = min(answer, make_rectangle(temp_x, temp_y))

print(answer)
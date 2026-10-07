n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
distance = float('inf')
for i in range(n):
    for j in range(i+1,n):
        x1,y1 = x[i],y[i]
        x2,y2 = x[j],y[j]
        a = abs(x1-x2)
        b = abs(y1-y2)
        distance = min(distance, a**2 + b**2)

print(distance)
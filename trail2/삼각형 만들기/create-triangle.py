n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
answer = 0

def check(x1,x2,x3,y1,y2,y3):
    x_cnt, y_cnt = 0,0
    if x1 == x2:
        x_cnt += 1
    if x2 == x3:
        x_cnt += 1
    if x3 == x1:
        x_cnt += 1
    if y1 == y2:
        y_cnt += 1
    if y2 == y3:
        y_cnt += 1
    if y3 == y1:
        y_cnt += 1
    
    if x_cnt == 1 and y_cnt == 1:
        return True
    return False


for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            x1,y1 = x[i],y[i]
            x2,y2 = x[j],y[j]
            x3,y3 = x[k],y[k]
            if check(x1,x2,x3,y1,y2,y3):
                area = abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))
                # print((x1,y1),(x2,y2),(x3,y3))
                answer = max(area,answer)

print(int(answer))
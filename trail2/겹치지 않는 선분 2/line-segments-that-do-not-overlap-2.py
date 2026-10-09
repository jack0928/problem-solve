n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 선분이 다른 하나의 선분과 교차하는지 확인하는 함수
def check_cross(line1, line2):
    a1,a2 = line1[0],line1[1]
    b1,b2 = line2[0],line2[1]

    if (a1 <= b1 and a2 >= b2) or (a1 >= b1 and a2 <= b2):
        return True
    return False

answer = 0

for i in range(n):
    cross_flag = False
    for j in range(n):
        if cross_flag:
            break
        if i != j:
            if check_cross(lines[i],lines[j]):
                cross_flag = True
                break
    if not cross_flag:
        answer += 1

print(answer)

        

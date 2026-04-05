'''
그냥 구현 문제
'''

# 시계 방향 회전
def rotate_clockwise(wheel):
    tmp = wheel[-1]
    for i in range(7, 0, -1):
        wheel[i] = wheel[i-1]
    wheel[0] = tmp

# 반시계 방향 회전
def rotate_anti_clockwise(wheel):
    tmp = wheel[0]
    for i in range(7):
        wheel[i] = wheel[i+1]
    wheel[7] = tmp

# 전체 회전
def rotate(index, direction, wheel_list):
    index -= 1  # 0-based로 변환

    # 각 톱니의 회전 방향 저장
    directions = [0] * 4
    directions[index] = direction

    # 왼쪽 전파
    for i in range(index, 0, -1):
        if wheel_list[i][6] != wheel_list[i-1][2]:
            directions[i-1] = -directions[i]
        else:
            break

    # 오른쪽 전파
    for i in range(index, 3):
        if wheel_list[i][2] != wheel_list[i+1][6]:
            directions[i+1] = -directions[i]
        else:
            break

    # 한 번에 회전
    for i in range(4):
        if directions[i] == 1:
            rotate_clockwise(wheel_list[i])
        elif directions[i] == -1:
            rotate_anti_clockwise(wheel_list[i])

def get_score(wheel_list):
    answer = 0
    for i in range(4):
        wheel = wheel_list[i]
        if wheel[0] == 1:
            answer += 2**i

    return answer

gearwheel_1 = list(map(int, input())) # 2번 톱니
gearwheel_2 = list(map(int, input())) # 2번, 6번
gearwheel_3 = list(map(int, input())) # 2번, 6번
gearwheel_4 = list(map(int, input())) # 6번
wheels = [gearwheel_1,gearwheel_2,gearwheel_3,gearwheel_4]

k = int(input()) # 회전 횟수
rotations = []

for _ in range(k):
    wheel_num, direction = map(int, input().split())
    rotations.append((wheel_num, direction))

for wheel_to_be_rotated, rotation_direction in rotations:
    # 회전
    rotate(wheel_to_be_rotated, rotation_direction, wheels)

# 총합 계산
print(get_score(wheels))
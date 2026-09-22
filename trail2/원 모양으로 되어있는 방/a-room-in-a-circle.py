n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
# 특정 방 기준 계산 함수
def calculate_distance(start):
    total = 0
    for i in range(n):
        distance = i - start 
        if distance < 0: # 반시계방향만 가능
            distance = n + distance
        total += distance * a[i]
    
    return total

# N개의 방을 돌아가며 하나씩 출발방으로 지정 후 계산
answer = 10 ** 99
for i in range(n):
    answer = min(answer, calculate_distance(i))

print(answer)
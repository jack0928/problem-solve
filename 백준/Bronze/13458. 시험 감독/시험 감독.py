import math

n = int(input())
participants = list(map(int, input().split()))
b,c = map(int, input().split())
answer = n

for num in participants:
    if num > b:
        answer += math.ceil((num-b)/c)

print(answer)
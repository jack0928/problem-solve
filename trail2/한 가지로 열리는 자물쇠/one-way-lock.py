N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
answer = 0
for x in range(1, N+1):
    for y in range(1, N+1):
        for z in range(1, N+1):
            if abs(x-a) <= 2 or abs(y-b) <= 2 or abs(z-c) <= 2:
                answer += 1

print(answer)
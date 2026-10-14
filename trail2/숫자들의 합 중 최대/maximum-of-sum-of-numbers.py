X, Y = map(int, input().split())

# Please write your code here.
answer = 0
for num in range(X,Y+1):
    total = 0
    for x in str(num):
        total += int(x)
    answer = max(answer, total)

print(answer)
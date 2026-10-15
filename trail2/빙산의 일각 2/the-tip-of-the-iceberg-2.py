n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.
# 덩어리의 개수 구하는 함수
def count_chunk(arr):
    cnt = 0
    if arr[0] > 0:
        cnt += 1

    for i in range(1,len(arr)):
        if arr[i] > 0 and arr[i-1] <= 0:
            cnt += 1

    return cnt

answer = 0
for s in range(min(h)-1, max(h)+1+1):
    new_h = h[:]
    for i in range(n):
        new_h[i] -= s
    answer = max(answer, count_chunk(new_h))

print(answer)
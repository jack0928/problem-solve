N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
answer = 10**9
for i in range(N-1):
    for j in range(i+1,N):
        temp = arr[0:i] + arr[i+1:j] + arr[j+1:N]
        answer = min (answer, abs(S - sum(temp)))

print(answer)
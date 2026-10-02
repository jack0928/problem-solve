N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_cost = float('inf')

for start in range(N - T + 1):
    subsegment = arr[start : start + T]
    current_cost = sum(abs(x - H) for x in subsegment)
    min_cost = min(min_cost, current_cost)

print(min_cost)
abilities = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations
answer = 10**9

arr = list(combinations(abilities, 3))

total = sum(abilities)

for i in range(20):
    result = abs(sum(arr[i]) - (total - sum(arr[i])))
    answer = min(answer, result)

print(answer)
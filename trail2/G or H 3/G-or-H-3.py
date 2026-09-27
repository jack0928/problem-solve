n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
arr = []
for i in range(len(x)):
    arr.append((x[i], c[i]))

def calculate_score(i,k,arr):
    score = 0
    for pos, sign in arr:
        if pos >= i and pos <= i+k:
            if sign == 'G':
                score += 1
            elif sign == 'H':
                score += 2
            else:
                continue 
    return score

answer = 0
for i in range(max(x)):
    answer = max(answer, calculate_score(i,k,arr))

print(answer)
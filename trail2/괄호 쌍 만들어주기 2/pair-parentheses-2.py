A = input()

# Please write your code here.
answer = 0
length = len(A)
for i in range(length - 3):
    if A[i] == A[i+1] and A[i] == '(':
        for j in range(i, length-1):
            if A[j] == A[j+1] and A[j] == ')':
                answer += 1

print(answer)
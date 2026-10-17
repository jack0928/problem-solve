X, Y = map(int, input().split())

# Please write your code here.
def check_palindrome(num):
    num = str(num)
    for i in range(len(num)//2):
        if not num[i] == num[len(num)-i-1]:
            return False
    return True

answer = 0
for num in range(X,Y+1):
    if check_palindrome(num):
        answer += 1

print(answer)
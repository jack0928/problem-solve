T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
# 특별한 위치인지 확인하는 함수
def check_special(k,c,x):
    d_1,d_2 = float('inf'),float('inf')
    for i in range(T):
        if c[i] == 'S':
            d_1 = min(d_1, abs(x[i] - k))
        else: # c[i] == 'N
            d_2 = min(d_2, abs(x[i] - k))
    if d_1 <= d_2:
        return True

answer = 0 
for k in range(a,b+1):
    if check_special(k,c,x):
        answer += 1

print(answer)
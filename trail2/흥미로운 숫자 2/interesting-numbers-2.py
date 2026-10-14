X, Y = map(int, input().split())

# Please write your code here.
# 포함된 숫자가 2종류고, 그 중 하나가 1개만 있으면 흥미로움
def is_interesting(num):
    # 포함된 숫자 확인
    num_list = list(str(num))
    num_set = list(set(num_list))
    if len(num_set) == 2:
        if num_list.count(num_set[0]) == 1 or num_list.count(num_set[1]) == 1:
            return True
    return False

answer = 0

for num in range(X,Y+1):
    if is_interesting(num):
        answer += 1

print(answer)
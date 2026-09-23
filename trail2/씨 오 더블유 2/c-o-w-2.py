n = int(input())
S = input()

# Please write your code here.
# C 뒤에 O가 있는 경우의 수 * 해당 O 뒤에 W가 있는 경우의 수
c_count = 0

co_count = 0

cow_count = 0

for ch in S:

    if ch == 'C':

        c_count += 1

    elif ch == 'O':

        # 지금 O 앞에 있던 모든 C와 CO를 만들 수 있음

        co_count += c_count

    elif ch == 'W':

        # 지금 W 앞에 있던 모든 CO와 COW를 만들 수 있음

        cow_count += co_count

print(cow_count)
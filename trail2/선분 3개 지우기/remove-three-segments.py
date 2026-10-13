n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.
# 여러 선분들이 겹치는지 확인하는 함수
def check_not_overlapped(n,l,r):
    for i in range(n-1):
        for j in range(i+1,n):
            if l[i] <= r[j] and r[i] >= l[j]:
                return False
    return True

# 3가지를 지우는 모든 경우의 수를 확인
answer = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            new_l,new_r = l[:],r[:]
            indices = [i,j,k]  # 제거하고 싶은 인덱스

            # 내림차순 정렬 후 하나씩 삭제 (그래야 안 밀림)
            for i in sorted(indices, reverse=True):
                del new_l[i]
                del new_r[i]

            if check_not_overlapped(n-3,new_l,new_r):
                answer += 1

print(answer)
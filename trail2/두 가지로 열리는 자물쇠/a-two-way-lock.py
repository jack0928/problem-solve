N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
# N이 5 이하이면 모든 조합(N^3개)이 가능함
if N <= 5:
    print(N ** 3)
else:
    # 1~N 범위 내에서 1-indexed 원형 이동 계산 함수
    def get_cand(x):
        # x-2, x-1, x, x+1, x+2 범위
        return [((x + i - 1) % N) + 1 for i in range(-2, 3)]

    cands1_a, cands1_b, cands1_c = get_cand(a1), get_cand(b1), get_cand(c1)
    cands2_a, cands2_b, cands2_c = get_cand(a2), get_cand(b2), get_cand(c2)

    valid_combos = set()

    # 첫 번째 조합 기준 가능한 모든 조합 (최대 125개)
    for i in cands1_a:
        for j in cands1_b:
            for k in cands1_c:
                valid_combos.add((i, j, k))

    # 두 번째 조합 기준 가능한 모든 조합 (최대 125개)
    for i in cands2_a:
        for j in cands2_b:
            for k in cands2_c:
                valid_combos.add((i, j, k))

    print(len(valid_combos))



'''
기존 코드는 시간 초과 발생
-> $N^3$개 조합을 모두 확인하는 대신, 
첫 번째 비밀번호 주변의 가능한 자물쇠 조합과 두 번째 비밀번호 주변의 가능한 자물쇠 조합만 
- 거리 2 이내에 들어오는 숫자는 각 자리당 최대 5개(-2, -1, 0, +1, +2) 뿐
- N <= 5인 경우: 어느 숫자를 골라도 거리가 2 이하가 되므로 전체 조합 수 N^3이 답
- N > 5인 경우: 각 자리당 가능한 숫자는 5개씩이므로, 하나의 비밀번호에 대해 최대 5^3 = 125가지 조합만 생성
-> 두 비밀번호에서 만들어지는 조합을 set에 담아 합집합의 크기(len)를 구하면 끝

# 단일 자리 거리 검사 함수
def distance(n, num, target):
    diff = abs(num - target)
    return min(diff, n - diff)

# 조합과의 거리 검사 함수, abs
def check(num1, num2, num3, comb):
    dist1 = distance(N, num1, comb[0])
    dist2 = distance(N, num2, comb[1])
    dist3 = distance(N, num3, comb[2])
    return dist1 <= 2 and dist2 <= 2 and dist3 <= 2

answer = 0

# combinations로 해도 됨
for num1 in range(1,N+1):
    for num2 in range(1,N+1):
        for num3 in range(1,N+1):
            if check(num1,num2,num3, [a1,b1,c1]): # 첫번째 조합 검사
                answer += 1
            elif check(num1,num2,num3, [a2,b2,c2]): # 두번째 조합 검사
                answer += 1
            else:
                continue


print(answer)
'''
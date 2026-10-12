N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.
# 배가 아팠던 사람은 확실히 상한 치즈를 먹은 사람 -> 이 사람이 먹은 치즈가 상한 치즈
# 아팠던 사람 모두가 먹었어야 상한 치즈
# 상한 치즈가 될 수 있는 후보들을 뽑은 뒤, 그 중에서 해당 치즈를 먹은 인원 수가 '최대'인 치즈의 인원수가 정답

# 특정 사람이 아팠던 시간을 가지고 그 사람이 그 앞에 먹은 치즈들은 전부 후보로
# 모든 치즈를 초기 후보로 설정
candidates = set(range(1, M + 1))

for i in range(S):
    sick_person, sick_time = sick_p[i], sick_t[i]
    eaten = set()
    for j in range(D):
        if p[j] == sick_person and t[j] < sick_time:
            eaten.add(m[j])

    # 아픈 모든 사람이 먹은 치즈만 후보로 남김
    candidates &= eaten

# 치즈별로 먹은 사람을 집합으로 관리
cnt = [set() for _ in range(M + 1)]

for i in range(D):
    if m[i] in candidates:
        cnt[m[i]].add(p[i])

answer = 0

for milk in candidates:
    answer = max(answer, len(cnt[milk]))

print(answer)
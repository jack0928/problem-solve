n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
answer = 0

# 1~9 사이의 숫자만 사용 (0 제외)
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            # 세 숫자가 모두 서로 다른 경우만 검사
            if i == j or j == k or i == k:
                continue

            flag = True
            for x in range(n):
                if not flag:
                    break
                
                num, cnt1, cnt2 = a[x], b[x], c[x]
                
                # 정수형 num을 3자리 문자열로 변환 (예: 12 -> "012")
                num_str = str(num).zfill(3)
                check1, check2 = 0, 0

                if i == int(num_str[0]):
                    check1 += 1
                elif str(i) in num_str:
                    check2 += 1

                if j == int(num_str[1]):
                    check1 += 1
                elif str(j) in num_str:
                    check2 += 1

                if k == int(num_str[2]):
                    check1 += 1
                elif str(k) in num_str:
                    check2 += 1

                # 1번이라도 조건(스트라이크, 볼 수)이 다르면 탈락
                if not (check1 == cnt1 and check2 == cnt2):
                    flag = False

            # N개의 질문을 모두 만족한 수만 정답에 추가
            if flag:
                answer += 1 

print(answer)
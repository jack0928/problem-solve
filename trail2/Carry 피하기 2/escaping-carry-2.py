n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
answer = -1

for i in range(n):

    for j in range(i + 1, n):

        for k in range(j + 1, n):

            a = arr[i]

            b = arr[j]

            c = arr[k]

            possible = True

            # ai <= 10000이므로 최대 5자리 확인

            for _ in range(5):

                if a % 10 + b % 10 + c % 10 >= 10:

                    possible = False

                    break

                a //= 10

                b //= 10

                c //= 10

            if possible:

                answer = max(answer, arr[i] + arr[j] + arr[k])

print(answer)
board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
# 가로 확인 함수
def check_horizontal(board, color):
    n = len(board)
    for i in range(n):
        for j in range(n - 4):
            num = 0
            for k in range(5):
                if board[i][j + k] != color:
                    break
                num += 1
            if num == 5:
                return color, i, j+2
    return 0, 0, 0

# 세로 확인 함수
def check_vertical(board, color):
    n = len(board)
    for i in range(n - 4):
        for j in range(n):
            num = 0
            for k in range(5):
                if board[i + k][j] != color:
                    break
                num += 1
            if num == 5:
                return color, i+2, j
    return 0, 0, 0

# 대각선 확인 함수 (좌상 -> 우하)
def check_diagonal_1(board, color):
    n = len(board)
    for i in range(n - 4):
        for j in range(n - 4):
            num = 0
            for k in range(5):
                if board[i + k][j + k] != color:
                    break
                num += 1
            if num == 5:
                return color, i+2, j+2
    return 0, 0, 0

# 대각선 확인 함수 (좌하 -> 우상)
def check_diagonal_2(board, color):
    n = len(board)

    # 시작점을 좌하단으로 잡고 우상단으로 이동
    for i in range(4, n):
        for j in range(n - 4):
            num = 0
            for k in range(5):
                if board[i - k][j + k] != color:
                    break
                num += 1
            if num == 5:
                # 가장 왼쪽 돌의 좌표
                return color, i-2, j+2
    return 0, 0, 0

answer = 0
x, y = 0, 0

# 검은색 확인
if answer == 0:
    answer, x, y = check_horizontal(board, 1)

if answer == 0:
    answer, x, y = check_vertical(board, 1)

if answer == 0:
    answer, x, y = check_diagonal_1(board, 1)

if answer == 0:
    answer, x, y = check_diagonal_2(board, 1)

# 흰색 확인
if answer == 0:
    answer, x, y = check_horizontal(board, 2)

if answer == 0:
    answer, x, y = check_vertical(board, 2)

if answer == 0:
    answer, x, y = check_diagonal_1(board, 2)

if answer == 0:
    answer, x, y = check_diagonal_2(board, 2)

if answer == 0:
    print(0)

else:

    print(answer)
    print(x + 1, y + 1)
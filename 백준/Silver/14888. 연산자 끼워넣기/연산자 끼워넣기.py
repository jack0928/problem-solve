'''
N이 최대인 경우 11일 때의 대략적인 최악의 경우는 연산자 개수가 고르게 분포(2,3,2,3)된 10!/(2!3!2!3!) =25200
따라서 브루트포스로 해결 가능 (주어진 시간 2초)
매 단계마다 선택 → 트리 구조 → DFS
'''
max_num = int(-1e9)
min_num = int(1e9)

n = int(input())
num_sequence = list(map(int, input().split()))
plus,minus,mul,div = map(int, input().split())

def dfs(index, current_value, plus, minus, mul, div):
    global max_num, min_num, n
    if index == n:
        max_num = max(max_num, current_value)
        min_num = min(min_num, current_value)
        return

    if plus > 0:
        dfs(index+1, current_value + num_sequence[index], plus-1, minus, mul, div)

    if minus > 0:
        dfs(index+1, current_value - num_sequence[index], plus, minus-1, mul, div)

    if mul > 0:
        dfs(index+1, current_value * num_sequence[index], plus, minus, mul-1, div)

    if div > 0:
        # 나눗셈 처리 주의
        if current_value < 0:
            dfs(index + 1, -(abs(current_value) // num_sequence[index]), plus, minus, mul, div - 1)
        else:
            dfs(index+1, current_value // num_sequence[index], plus, minus, mul, div-1)

dfs(1, num_sequence[0], plus, minus, mul, div)

print(max_num)
print(min_num)



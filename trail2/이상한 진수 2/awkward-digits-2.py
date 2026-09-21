a = input()

reversed_a = a[::-1]

# 가장 처음 나오는 '0'을 '1'로 1번만 변경
if '0' in a:
    a = a.replace('0', '1', 1)  # "1010" -> "1110"
else:
    reversed_a = reversed_a.replace('1', '0', 1)
    a = reversed_a[::-1]
    
# 2진수 문자열을 10진수 정수로 변환
result = int(a, 2)  # "1110" -> 14

print(result)
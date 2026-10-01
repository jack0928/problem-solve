n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
arr = []
for i in range(n):
    arr.append((pos[i],alpha[i]))

arr.sort()

new_pos = []
new_alpha = []
for p,a in arr:
    new_pos.append(p)
    new_alpha.append(a)

answer = 0
for left in range(n):
    for right in range(left, n):
        pic_size = new_pos[right] - new_pos[left]
        
        sub = new_alpha[left:right+1]
        cnt_g = sub.count('G')
        cnt_h = sub.count('H')
        
        # 1. G만 있거나 2. H만 있거나 3. G와 H 개수가 같을 때
        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            answer = max(answer, pic_size)

print(answer)
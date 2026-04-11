import copy
import sys
from collections import deque
from itertools import combinations

n,m = map(int, sys.stdin.readline().split())
lab = [[]for _ in range(n)]
global ans
ans = 0
res = 0
for i in range(n):
    lab[i] = list(map(int, sys.stdin.readline().split()))
org = copy.deepcopy(lab)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def infect(x,y): #감염시키는 함수 BFS
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if lab[nx][ny] == 1:
                continue
            if lab[nx][ny] == 0:
                lab[nx][ny] = 2
                queue.append((nx,ny))
    return False
        

empty = []
virus = []


#벽 3개 세우고 바이러스 있는 곳에만  바이러스 함수 돌려보고 0 개수 구하기
for i in range(n): #빈칸의 위치 정보
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i,j))

for i in range(n): #바이러스의 위치 정보
    for j in range(m):
        if lab[i][j] == 2:
            virus.append((i,j))
wall = list(combinations(empty,3))


for walls in wall:
    first,second,third = walls
    a,b = first[0],first[1]
    c,d = second[0],second[1]
    e,f = third[0], third[1]
    lab[a][b] = 1
    lab[c][d] = 1
    lab[e][f] = 1
    for i in range(len(virus)): #벽을 세운 후 바이러스 감염시키기
        x,y = virus[i][0], virus[i][1]
        infect(x,y)
    res = 0
    for i in range(n): #안전 영역 크기 확인
        for j in range(m):
            if lab[i][j] == 0:
                res += 1
                
    ans = max(ans, res) #최댓값으로 갱신
    lab = copy.deepcopy(org) #벽 없애기

    

print(ans)
# 일부 케이스 통과한 코드

''' 대략적인 문제 내용
위애서 아래로 가는데 좌우로 가장 적게 움직이기
'''

from collections import deque


arr = []

def dfs(i, j, d):
    if arr[i+1][j+1] == "x":
        return
    if arr2[i][j] < d:
        return

    arr2[i][j] = d

    dfs(i+1, j, d)
    dfs(i, j+1, d+1)
    dfs(i, j-1, d+1)


m, n = map(int, input().split())
arr2 = [[float('inf') for _ in range(m)] for _ in range(n)]

arr.append(['x' for _ in range(m+2)])
for i in range(n):
    arr.append(['x'] + list(input()) + ['x'])
arr.append(['x' for _ in range(m+2)])

for j in range(m):
    if arr[1][j+1] == 'c':
        # dfs(0, j, 0)

        queue = deque()
        queue.appendleft((1, j+1, 0))
        while len(queue):
            i, j, d = queue.pop()

            
            if arr[i+1][j+1] == "x":
                continue
            if arr2[i][j] < d:
                continue

            arr2[i][j] = d

            queue.appendleft((i+1, j, d))
            queue.appendleft((i, j+1, d+1))
            queue.appendleft((i, j-1, d+1))        

print(min(arr2[n-1]))

# 모든 케이스 통과한 코드

''' 대략적인 문제 내용
어느 길로가야 가장 큰 값을 가지는가?
start : (1, 1)
goal : (n, m)
'''

from collections import deque
from copy import deepcopy


m, n = map(int, input().split())

arr = []
arr.append([float('inf') for _ in range(m+2)])
for i in range(n):
    arr.append([float('inf')] + list(map(int, input().split())) + [float('inf')])
arr.append([float('inf') for _ in range(m+2)])

arr2 = deepcopy(arr)

queue = deque()
queue.appendleft((n, m))
while len(queue):
    i, j = queue.pop()

    tmp = arr2[i][j] + arr[i-1][j]
    if tmp > arr2[i-1][j]:
        arr2[i-1][j] = tmp
        queue.appendleft((i-1, j))

    tmp = arr2[i][j] + arr[i][j-1]
    if tmp > arr2[i][j-1]:
        arr2[i][j-1] = tmp
        queue.appendleft((i, j-1))


print(arr2[1][1])

    

# case 1
''' input
3 5
3 4 5
2 3 9
3 9 3
4 5 1
1 3 6
'''

''' output
33
'''
# 모든 케이스 통과한 코드

''' 대략적인 문제 내용
정사각형이 몇개 들가냐?
'''

def check(i, j):
    s = 1

    while True:
        for x in range(i, i + s):
            for y in range(j, j + s):
                if arr[x][y] == 0:
                    return
        
        size[s] += 1
        s += 1


n = int(input())

arr = []
size = [0 for _ in range(n+1)]
total = 0

for i in range(n):
    arr.append(list(map(int, input())) + [0])
arr.append([0 for _ in range(n+1)])
    
for i in range(n):
    for j in range(n):
        check(i, j)

for i in size:
    total += i

print("total:", total)
for i in range(1, n+1):
    if size[i] == 0:
        break
    
    print("size[%d]: %d"%(i, size[i]))

# case 1
''' input
4
1110
1110
0110
0000
'''

''' output
total: 11
size[1]: 8
size[2]: 3
'''
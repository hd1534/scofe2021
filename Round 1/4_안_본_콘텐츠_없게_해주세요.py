# 모든 케이스 통과한 코드

''' 대략적인 문제 내용
그냥 정렬 문제
'''

stat = []
genre = []
arr_Y = []
arr_O = []

ABCDE = list(map(float, input().split()))

n, m = map(int, input().split())

for i in range(n):
    stat.append(input())
for i in range(n):
    genre.append(input())

for i in range(n):
    for j in range(m):
        if stat[i][j] == "Y":
            # 장르, 선호도(숫자), 행, 열
            arr_Y.append((genre[i][j], ABCDE[ord(genre[i][j]) - 65], i, j))
        if stat[i][j] == "O":
            # 장르, 선호도(숫자), 행, 열
            arr_O.append((genre[i][j], ABCDE[ord(genre[i][j]) - 65], i, j))


arr_Y.sort(key = lambda x: x[1], reverse=True)
arr_O.sort(key = lambda x: x[1], reverse=True)

for i in arr_Y:
    print("%s %.1f %d %d" % i)
for i in arr_O:
    print("%s %.1f %d %d" % i)


# case 1
''' input
4.0 3.0 2.1 4.3 5.0
2 3
WYO
YYO
ABC
DCE
'''

''' output
D 4.3 1 0
B 3.0 0 1
C 2.1 1 1
E 5.0 1 2
C 2.1 0 2
'''
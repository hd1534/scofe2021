# 모든 케이스 통과한 코드

''' 대략적인 문제 내용
사람들 시간 받아서 모두 가능한 시간 출력
'''

n = int(input())

start = "00:00"
end = "24:00"

for i in range(n):
    s, e = input().split(" ~ ")

    start = max(start, s)
    end = min(end, e)


if start > end:
    print(-1)
else:
    print(start, "~", end)


# case 1
''' input
3
12:00 ~ 23:59
11:00 ~ 18:00
14:00 ~ 20:00
'''

''' output
14:00 ~ 18:00
'''

# 모든 케이스 통과한 코드

''' 대략적인 문제 내용
한칸 가거나 두칸 가거나
'''

memo = [-1 for _ in range(60)]

def recursive(i):
    if i == 2:
        return 1
    if i == 1:
        return 1
    
    if memo[i] == -1:
        memo[i] = recursive(i-1) + recursive(i-2)

    return memo[i]

n = int(input())

arr = input().split("0")

result = 1

for i in arr:
    result *= recursive(len(i))

print(result)


# case 1
''' input
3
111
'''

''' output
2
'''

# case 2
''' input
4
1101
'''

''' output
1
'''

# case 3
''' input
5
11111
'''

''' output
5
'''
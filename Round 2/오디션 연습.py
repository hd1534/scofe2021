
n, time = input().split()
n = int(n)
h, m, s = map(int, time.split(":"))
time = s + m * 60 + h * 3600
arr = []

for i in range(n):
    m, s = map(int, input().split(":"))
    arr.append(s + m * 60)    

max = 0
max_p = 0
for i, _ in enumerate(arr):
    tmp = time
    count = 1
    
    for j in arr[i:]:
        tmp -= j
        if tmp <= 0:
            break
        
        count += 1
    else:
        count -= 1

    if count > max:
        max = count
        max_p = i


print(max, max_p + 1)



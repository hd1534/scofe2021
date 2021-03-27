from copy import deepcopy

arr = []

def find(a, b):
    global arr
    
    for i in arr[b]:
        arr[a].add(i)
        find(a, i)


def sol():
    global arr
    n, q = map(int, input().split())    
    arr = [set([]) for i in range(n+10)]

    for i in range(n-1):
        a, b = map(int, input().split())
        arr[a].add(b)

    # 기록
    for i in range(n+10):
        tmp = deepcopy(arr[i])
        for j in tmp:
            find(i, j)

    for i in range(q):
        a, b = map(int, input().split())
        print("yes" if b in arr[a] else "no")


if __name__ == "__main__":
    sol()
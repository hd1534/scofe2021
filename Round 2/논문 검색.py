
def sol():
    arr = []
    for i in range(int(input())):
        arr.append(input())
    
    for i in range(int(input())):
        s = input()
        count = 0

        for j in arr:
            if s in j:
                count += 1
        
        print(count)



if __name__ == "__main__":
    sol()
t = int(input())
for i in range(t):
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    total = sum(arr)
    print(total, end=' ')
    for j in range(n-1):
        total -= arr[j]
        print(total,end =' ')
    print()
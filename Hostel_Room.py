t = int(input())
for i in range(t):
    n,a = map(int,input().split())
    maxi = a
    arr = list(map(int,input().split()))
    for i in arr:
        a+=i
        maxi = max(maxi,a)
    print(maxi)
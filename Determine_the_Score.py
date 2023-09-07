t = int(input())
for i in range(t):
    x,n = map(int, input().split())

    if(x%10 == 0):
        ans = x//10
        print(ans*n)
    else:
        print("0")
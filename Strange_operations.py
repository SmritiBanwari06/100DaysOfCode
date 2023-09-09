t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    x = sum(list(map(int,input().split())))
    if (x%2==0 and k==1):
        print("odd")
    else:
        print("even")
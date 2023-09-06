t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    if (n%2==0):
        print("YES")
    else:
        if(x%2==0):
            print("NO")
        else:
            print("YES")
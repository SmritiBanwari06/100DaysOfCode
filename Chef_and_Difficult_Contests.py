t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    d = 1
    if(abs(a-b))/((2*d)-1)!=0:
        print("YES")
    else:
        print("NO")
t = int(input())
for i in range(t):
    s,a,b,c = map(int,input().split())
    d = (100+c)/100*s
    if(d>=a and d<=b):
        print("Yes")
    else:
        print("No")
t = int(input())
for i in range(t):
    p1,p2,k = map(int,input().split())
    if((p1+p2)//k%2):
        print("COOK")
    else:
        print("CHEF")
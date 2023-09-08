t = int(input())
for i in range(t):
    abc = list(map(int,input().split()))
    if(abc.count(min(abc))>=2 ):
        print("YES")
    else:
        print("NO")
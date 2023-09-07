t = int(input())
for i in range(t):
    m,n = map(int,input().split())
    a = 0
    for i in range(0,m,2):
        for j in range(0,n,2):
            a +=1
    print(a)
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    print(x%(n+1))
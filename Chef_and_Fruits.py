t = int(input())
for i in range(t):
    n,m,k = map(int,input().split())
    print(max(abs(n-m)-k,0))
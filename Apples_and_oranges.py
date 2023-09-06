t = int(input())
for i in range(t):
    n,m  = map(int,input().split())
    def aao(n,m):
        if(m==0):
            return n
        else:
            return aao(m,n%m)
    AAO = aao(n,m)
    print(AAO)
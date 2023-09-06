t = int(input())
for i in range(t):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in a:
        if(m-i+1<k):
            print('No')
            break
    else:
        print('Yes')

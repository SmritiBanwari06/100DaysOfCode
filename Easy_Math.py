t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = 0
    for i in range(n-1):
        for j in range(i+1,n):
            product = a[i]*a[j]
            digit = [int(x) for x in str(product)]
            if sum(digit)>b:
                b = sum(digit)

    print(b)
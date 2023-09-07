t = int(input())
for i in range(t):
    n = int(input())
    l  =list(map(int,input().split()))
    x = 0
    count = 0
    for j in l:
        k = l.count(j)
        if k>=3:
            x +=1
    print("No" if x>1 else "Yes")
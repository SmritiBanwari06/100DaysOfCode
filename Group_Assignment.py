t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int,input().split()))
    group = set(p)
    for g in group:
        if p.count(g) % g!=0:
            print("NO")
            break
    else:
        print("YES")
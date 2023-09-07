t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    x = 0
    s =set()
    for i in range(n):
        if(l[i]) in s:
            s.remove(l[i])
        else:
            s.add(l[i])
        
        x = max(x,len(s))
    print(x)
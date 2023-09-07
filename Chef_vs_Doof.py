t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a_odd = list(filter(lambda x: x%2 !=0,a))

    if len(a_odd) ==n:
        print("YES")
    else:
        print("NO")
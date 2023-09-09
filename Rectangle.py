t = int(input())
for i in range(t):
    len = list(map(int,input().split()))
    len.sort()
    if len[0] == len[1] and len[2]== len[3]:
        print("YES")
    else:
        print("NO")
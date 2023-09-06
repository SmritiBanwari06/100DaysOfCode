t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    s = list(input())
    a = [x]

    for i in s:
        if i=="R":
            a.append(a[-1] + 1)
        else:
            a.append(a[-1]-1)
    print(len(set(a)))

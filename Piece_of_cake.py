t = int(input())
for i in range(t):
    a = input()
    for i in a:
        if a.count(i) == len(a) -a.count(i):
            print("YES")
            break
    else:
        print("NO")
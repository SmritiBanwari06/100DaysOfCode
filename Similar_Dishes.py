t = int(input())
for i in range(t):
    x = list(input().split())
    y = list(input().split())
    z  =0
    for i in x:
        if i in y:
            z +=1
            if z ==2:
                print("similar")
                break
    else:
        print("dissimilar")
            
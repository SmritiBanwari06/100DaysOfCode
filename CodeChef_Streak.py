t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    oc = 0
    ac = 0
    os = oc
    a_s = ac
    for i in range(n):
        if a[i] !=0:
            oc += 1
        else:
            oc = 0

        if b[i] != 0:
            ac += 1
        else:
            ac =0
        os = max(oc,os)
        a_s = max(ac,a_s)

    if(os>a_s):
        print("Om")
    elif(os<a_s):
        print("Addy")
    else:
        print("Draw")

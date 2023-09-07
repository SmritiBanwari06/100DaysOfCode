t = int(input())
for i in range(t):
    s = input()
    x = 0
    y = ['c','e','f','h']
    for j in range(len(s)):
        if sorted(s[j:j+4])==y:
            x+=1
    if x ==0:
        print("normal")
    else:
        print('lovely ' + str(x))

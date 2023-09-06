t = int(input())
for i in range(t):
    s = input()
    a = s.count("xy")
    b = s.replace("xy","")
    c = b.count("yx")
    print((a+c))
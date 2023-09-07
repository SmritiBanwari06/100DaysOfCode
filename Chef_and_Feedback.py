t = int(input())
for i in range(t):
    s = input()
    if(s.count('101') or s.count('010')):
        print("Good")
    else:
        print("Bad")
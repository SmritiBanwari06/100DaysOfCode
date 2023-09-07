# t = int(input())
# for i in range(t):
#     n= int(input())
#     finger = list(map(int,input().split()))
#     glove = list(map(int,input().split()))

#     front_possible = True
#     back_possible= True

#     for i in range(n):
#         if finger[i]>glove[i]:
#             front_possible = False
#         if front_possible[i] >glove[n-1-i]:
#             back =False

#     if front_possible and back_possible:
#         print("Both")
#     elif front_possible:
#         print("Front")
#     elif back_possible:
#         print("Back")
#     else:
#         print("none")
# cook your dish here

for _ in range(int(input())):
    n = int(input())
    f_len = list(map(int, input().split()))
    glove_len = list(map(int, input().split()))

    front_possible = True
    back_possible = True

    for i in range(n):
        if f_len[i] > glove_len[i]:
            front_possible = False
        if f_len[i] > glove_len[n - 1 - i]:
            back_possible = False

    if front_possible and back_possible:
        print("both")
    elif front_possible:
        print("front")
    elif back_possible:
        print("back")
    else:
        print("none")
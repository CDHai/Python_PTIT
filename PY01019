from ntpath import join
import string

t = int(input())
while(t > 0):
    t -=1
    s1 = input()
    s2 = list(reversed(s1))
    s2 = "".join(s2)
    x = 1
    for i in range(1,len(s1)-1):
        if (abs(ord(s1[i])-ord(s1[i-1])) == abs(ord(s2[i])-ord(s2[i-1]))):
            continue
        else:
            x = 0
            break
    if (x == 0):
        print("NO")
    else:
        print("YES")




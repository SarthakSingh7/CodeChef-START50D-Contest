for i in range(int(input())):
    tc =input().split()
    x = int(tc[0])
    y = int(tc[1])
    z = int((x+y)/2)
    c1 = abs(x-z)
    c2 = abs(y-z)
    fi = max(c1,c2)
    print(fi)

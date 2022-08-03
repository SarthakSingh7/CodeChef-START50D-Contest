for i in range(int(input())):
    tc = input().split()  # N X Y A B
    N = int(tc[0])  # distance in km
    X = int(tc[1])  #petrol cost per litre
    Y = int(tc[2])  #diesel cost per litre
    A = int(tc[3])  # dist in 1 l petrol
    B = int(tc[4])  # dist with 1 l of diesel
    cost_p = (X/A)*N # cost per km * distance = total cost 
    cost_d = (Y/B)*N
    if cost_p > cost_d:
        print('DIESEL')
    if cost_p <cost_d:
        print('PETROL')
    if cost_p == cost_d:
        print('ANY')
    

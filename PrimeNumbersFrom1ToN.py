N = int(input())
for i in range(2,N):
    flag = 0
    for j in range(2,i):
        if (i % j == 0):
            flag = 1
    if (flag == 0):
        print (i)

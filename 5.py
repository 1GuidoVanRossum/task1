k = 0
s = 0
l = []
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(1 , n):
            if i > 9:
                break
            if i % 2 != 0:
                k = k + i
            else:
                k = k - i
        if n > 9:
            for i in range(10 , n+1):
                s = i
                l = tuple(str(s))
                for j in range(len(l)):
                    if j % 2 == 0:
                        k = k - int(l[j])
                    else:
                        k = k + int(l[j])
    print(k)


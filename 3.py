
n = int(input())
l = []
l1 = []
for i in range(n):
    l1 = list(map(int , input().split()))
    num1 = l1[0]
    num2 = l1[1]
    if num1 == 1:
        num1 = num1 + 1
    for i in range(num1, num2+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            l.append(i)
print(*l , sep = "\n")

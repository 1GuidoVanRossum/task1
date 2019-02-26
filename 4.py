n = int(input())
l = []
for  i in range(n):
    s1 = int(input())
    s1 = s1 + 1
    k = str(s1)
    s2 = k[::-1]
    while s2 != k:
        s1 = s1 + 1
        k = str(s1)
        s2 = k[::-1]
    l.append(k)
print('\n'.join(l))
        

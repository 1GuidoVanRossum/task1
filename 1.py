n = int(input())
l = []
k1 = 0
s = []
for i in range(n):
    l.append(input())
for i in range(n):
    g = tuple(l[i])
    k = len(g)//2
    s.append(''.join(g[0:k:2]))
        
    k1 = 0
print(*s, sep ='\n')

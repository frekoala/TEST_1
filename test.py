# -*- coding: utf-8 -*-

def triangles():
    L=[]
    L.append(1)
    while len(L)<11:
        yield(L)
        L.append(0)
        L=[L[j]+L[j-1] for j in range(len(L))]
    return 'done'

n = 0
results = []
for t in triangles():
    print('t=%s'%t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

print(results)